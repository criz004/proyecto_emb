"""
Programa simple de dibujo para la pantalla táctil ili9341
"""
import xpt2046_circuitpython # Controlador de panel táctil
import time
import busio
import digitalio
import board
from adafruit_rgb_display import color565 # Controlador de display
import adafruit_rgb_display.ili9341 as ili9341


# Configuración de pines para la comunicación
cs_d = digitalio.DigitalInOut(board.D8)
dc_d = digitalio.DigitalInOut(board.D22)
rst_d = digitalio.DigitalInOut(board.D5)

cs_t = digitalio.DigitalInOut(board.D17)
irq_t = digitalio.DigitalInOut(board.D26)

# Configuracioń de la comunicación SPI para dos puertos

spi_d = busio.SPI(clock=board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
spi_t = busio.SPI(clock = board.SCLK_1, MOSI = board.MOSI_1, MISO = board.MISO_1)

# Creando el objeto display para el control de la pantalla
display = ili9341.ILI9341(
            spi_d,
            rotation = 0,
            cs=cs_d,
            dc=dc_d,
            rst=rst_d,
            baudrate = 40000000)

# Creando el objeto touch para el control del panel táctil
touch = xpt2046_circuitpython.Touch(
            spi_t,
            cs = cs_t,
            interrupt = irq_t,
            force_baudrate = 4000000
)

# Limpiando la pantalla
display.fill(color565(0, 0, 0))
ancho = display.width
alto = display.height

print('Tamaño = ' , ancho, 'x', alto)

x_inv = 0
y = 0
while True:
    # Check if we have an interrupt signal
    if touch.is_pressed():
        # Erase las rectangle
        display.fill_rectangle(x_inv, y,3, 3, color565(0, 0, 0))
        # Get the coordinates for this touch.
        x, y = touch.get_coordinates()
        x_inv = ancho-x
        
        print(x,y)

        # The Y reading is flipped to what the Adafruit library expects.
        display.fill_rectangle(x_inv, y,3, 3, color565(255, 255, 255))

    # Delay for a bit
    time.sleep(0.1)

