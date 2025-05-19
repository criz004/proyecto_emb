'''Programa 0.- Menú de aplicaciones'''

def programa_0(display, touch, Boton):
    WIDTH, HEIGHT = display.width, display.height
    # Dibujando botones
    botones = []
    botones.append(Boton((0, 0*HEIGHT//3, WIDTH-1, 1*(HEIGHT)//3+1), (241, 196, 15), 'Integrantes', (0, 0, 0)))
    botones.append(Boton((0, 1*HEIGHT//3, WIDTH-1, 2*(HEIGHT)//3+1), (93, 173, 226), 'Temperatura Numérica', (0, 0, 0)))
    botones.append(Boton((0, 2*HEIGHT//3, WIDTH-1, 3*(HEIGHT)//3+1), (88, 214, 141), 'Temperatura Gráfica', (0, 0, 0)))
    for boton in botones:
        boton.dibuja()
    display.image(Boton.imagen)
    # Ejecutando y retornando
    while True:
        if touch.is_pressed():
            try:
                y,x_inv = touch.get_coordinates()
            except:
                continue
            x = WIDTH-x_inv
            print(x,y)
            if y <= (1*HEIGHT//3-1):
                estado = 1
            elif y <= (2*HEIGHT//3-1):
                estado = 2
            elif y <= (3*HEIGHT//3-1):
                estado = 3
            break
    return estado
