'''
Programa 1.- Muestra información del equipo e integrantes y sale si detecta un toque
'''

def programa_1(display, touch, Boton):

    WIDTH, HEIGHT = display.width, display.height

    # Dibujando botones
    texto = "PROYECTO FINAL\nIntegrantes:\nKarla \nCristopher \nAndy \nPana"
    boton = Boton((0, 0, WIDTH, HEIGHT), (0, 0, 0), 'Integrantes', (255, 255, 255))
    boton.dibuja()
    display.image(Boton.imagen)

    # Ejecutando y retornando
    while True:
        if touch.is_pressed():
            try:
                x_inv, y = touch.get_coordinates()
            except:
                continue
            x = WIDTH - x_inv
            print(x, y)
            estado = 0
            break
    return estado

