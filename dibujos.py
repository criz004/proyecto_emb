'''
Módulo para la gestión de los dibujos para la pantalla
'''

from PIL import Image, ImageDraw, ImageFont

# Crea la clase Imagen que contiene el dibujo a modificar, y la imagen asociada
class Imagen():
    imagen = Image.new("RGB", (240, 320)) # Cambiar a tamaño de la pantalla
    dibujo =  ImageDraw.Draw(imagen)
    fontsize =24
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", fontsize)

# Crea una clase Boton. Los atributos de clase de Imagen se heredan y son accesibles desde
# cualquier instancia de clase Boton
class Boton(Imagen):
    def __init__(self, coords, color, texto, color_texto):
        self.coords = coords
        self.color = color
        self.texto = texto
        self.color_texto = color_texto
    def dibuja(self):
        self.dibujo.rectangle(self.coords[::], fill = self.color)
        self.dibujo.text(self.coords[::], self.texto, fill = self.color_texto, font = self.font)
