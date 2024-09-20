from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C
import framebuf
import time
import random

# Define las dimensiones de la pantalla OLED
W = 128
H = 64
S=1
score=0
a=True
flag=True
D = Pin(27, Pin.IN, Pin.PULL_DOWN)
U = Pin(18, Pin.IN, Pin.PULL_DOWN)
R = Pin(11, Pin.IN, Pin.PULL_DOWN)
L = Pin(26, Pin.IN, Pin.PULL_DOWN)
C = Pin(19, Pin.IN, Pin.PULL_DOWN)

# Inicializa la comunicación I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Inicializa la pantalla OLED
oled = SSD1306_I2C(W, H, i2c)

# Define el buffer para un cuadrado de 3x3 bits (3 bytes)
buffer = bytearray([0b11100000, 0b11100000, 0b11100000])
with open ('Snake.pbm', 'rb') as f:
        f.readline()
        f.readline()
        f.readline()
        data=bytearray(f.read())
# Crea un objeto FrameBuffer con el buffer, de 3 píxeles de ancho y 3 de alto
fb = framebuf.FrameBuffer(buffer, 3, 3, framebuf.MONO_HLSB)
fbuf= framebuf.FrameBuffer(data,128,64,framebuf.MONO_HLSB)
    
# Variables de posición
snake = [(0, 0)]  # Lista de segmentos de la serpiente (tupla de coordenadas)
m = 0  # Dirección de movimiento (0: derecha, 1: izquierda, 2: abajo, 3: arriba)
xf = 0
yf = 0

def MovS():
    global m, xf, yf, score,S

    head_x, head_y = snake[0]  # La cabeza de la serpiente es el primer segmento
    # Movimiento
    if m == 0:
        head_x += 3
    elif m == 1:
        head_x -= 3
    elif m == 2:
        head_y += 3
    elif m == 3:
        head_y -= 3

    

    # Añade la nueva posición de la cabeza
    snake.insert(0, (head_x, head_y))

    # Si la serpiente no ha comido, elimina el último segmento
    if (head_x, head_y) != (xf, yf):
        snake.pop()
    else:
        score+=1
        food()  # Genera nueva comida

    Draw()

    # Verifica si la serpiente ha colisionado con ella misma o con los bordes
    if head_x < 0 or head_x >= 126 or head_y < 0 or head_y >= 63 or (head_x, head_y) in snake[1:]:
        print(head_x, head_y)
        GameOver()
    
def buttons(Pin):
    global S,a,m,flag
    if S==1:
        a=False
        S+=1
    elif S==2:
        if flag==True:
            flag=False
            # Condiciones para cambiar la dirección
            if Pin==U and m != 3:
                m = 2
            elif Pin==D and m != 2:
                m = 3
            elif Pin==R and m != 1:
                m = 0
            elif Pin==L and m != 0:
                m = 1
def Draw():
    # Limpia la pantalla
    oled.invert(0)
    oled.fill(0)
    # Dibuja los bordes
    oled.rect(0, 0, W, H, 1)  # Dibujar un rectángulo con el grosor del borde de 1 píxel

    # Dibuja cada segmento de la serpiente
    for segment in snake:
        oled.blit(fb, segment[0], segment[1])

    # Dibuja la comida
    oled.blit(fb, xf, yf)

    # Muestra el contenido actualizado en la pantalla OLED
    oled.show()

    # Retardo para observar el cambio
    time.sleep(0.1)

def GameOver():
    global snake,a,m,S,score,flag
    flag=True
    a = True
    while a==True:
        oled.fill(0)
        oled.text('Game Over', W // 2 - 40, H // 2 - 8)
        oled.show()
        time.sleep(0.5)
        Draw()
        time.sleep(0.5)
        S=1
    a=True
    flag=True
    while a==True:
        sc='Score: '+str(score)
        oled.fill(0)
        oled.text(sc, W // 2 - 40, H // 2 - 8)
        oled.show()
    a=True
    flag=True
    while a==True:
        # Reinicia el juego
        oled.fill(0)
        oled.text('Repeat?', W // 2 - 40, H // 2 - 8)
        oled.show()
        time.sleep(0.5)
        S=1
    score=0
    snake = [(0, 0)]
    m=0

def food():
    global xf, yf
    while True:
        xf = random.randint(0, (W - 3) // 3) * 3
        yf = random.randint(0, (H - 3) // 3) * 3
        if (xf, yf) not in snake and xf!=0 and yf!=0:
            break
            
def portada():
    global a
    while a==True:
        oled.invert(1)
        oled.blit(fbuf,0,0)
        oled.show()

def start():
    global m,flag
    food()
    while True:
        m = 0
        while True:
            MovS()
            flag=True

#interrupciones
U.irq(handler=buttons, trigger=Pin.IRQ_RISING)
D.irq(handler=buttons, trigger=Pin.IRQ_RISING)
R.irq(handler=buttons, trigger=Pin.IRQ_RISING)
L.irq(handler=buttons, trigger=Pin.IRQ_RISING)
portada()
start()