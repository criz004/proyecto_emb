'''
Módulo para la configuración de Hardware:
1) Comunicación SPI
2) Display ILI9341
3) Panel Táctil xpt2046

'''
import xpt2046_circuitpython
import time
import busio
import digitalio
import board
from adafruit_rgb_display import ili9341, color565

# Configurando pines de comunicación
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D22)
reset_pin = digitalio.DigitalInOut(board.D5)
cs_t = digitalio.DigitalInOut(board.D17)
irq_t = digitalio.DigitalInOut(board.D26)

# Configuración de los puertos de comunicación SPI
spi_d = busio.SPI(clock=board.SCLK, MOSI=board.MOSI, MISO=board.MISO)
spi_t = busio.SPI(clock = board.SCLK_1, MOSI = board.MOSI_1, MISO = board.MISO_1)

# Creando el objeto display para el manejo de la pantalla
display = ili9341.ILI9341(
    spi_d,
    rotation = 0,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=40000000,
)
# Creando el objeto touch para el manejo del panel táctil
touch = xpt2046_circuitpython.Touch(
            spi_t,
            cs = cs_t,
            interrupt = irq_t,
            force_baudrate = 4000000
)

