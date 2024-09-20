# Cyber Security Week 2024 Badge
Repositorio para la badge creada para el Cyber Security Week 2024 de puma hat, esperen actualizaciones, nuevos juegos y si quieren colaborar siempre son bienvenidos.
## Requerimientos
Actualmente el código está disenado para una Raspberry pi pico con micropyhon, el hardware se puede visualizar con KiCad o cualquier aplicación compatible.
Se necesita en el circuito 5 push buttons y un OLED SSD1306.
Alguna forma de cargar los archivos a la Raspberry pi pico o Ide de micropython de preferencia se recomienda Thonny.
Un cable micro USB a USB para cargar los programas a la Raspberry pi pico o alimentarla con 5V, funciona con pilas de celular, el mismo celular o una computadora.
## Instalación
Nota: Se asume que ya cumple con los requerimientos y tiene cuando menos una protoboard con el circuito armado
- Dirigirse a la carpeta /Code/Scripts/Snake
- Descargar el main.py (Que es donde está todo el código del juego)
- Descagar ssd1306.py (la biblioteca para el control del OLED por I2C)
- Dirigirse a la carpeta /Code/Assets
- Descargar las imágenes .pbm existentes (Es la información de la parte gráfica que no fue programada como portadas y arte)
- Usar Thonny o ide de preferencia para cargar todos los archivos a la Raspberry pi pico
## Circuito
![image](https://github.com/user-attachments/assets/7fff954b-f88d-46f3-be25-e5a5aa0d534f)
