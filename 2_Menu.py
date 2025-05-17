'''Programa que entra a diferentes estados con diferentes aplicaciones'''

from configuracion import display, touch
from dibujos import Boton
from programa0 import programa_0
from programa1 import programa_1
from programa2 import programa_2
from programa3 import programa_3

estado = 0
while True:
    if estado == 0:
        estado = programa_0(display, touch, Boton)
    elif estado == 1:
        estado = programa_1(display, touch, Boton)
    elif estado == 2:
        estado = programa_2(display, touch, Boton)
    elif estado == 3:
        estado = programa_3(display, touch, Boton)
