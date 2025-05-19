''' Programa 2.- Temperatura Numérica'''

from bluetooth_reader import read_bluetooth
import threading

def programa_2(display, touch, Boton):
    WIDTH, HEIGHT = display.width, display.height
    
    # Variables para almacenar temperaturas
    temperaturas = []
    temp_actual = None #Variable auxiliar xP
    
    # Función para leer Bluetooth en segundo plano
    def update_temperature():
        nonlocal temp_actual, temperaturas #Variables para usarse en los otros programas XP
        for temp, temp_list in read_bluetooth(): #Itera los datos que devuelve el bluetoth_reader
            # Canjeo xdd a variables auxiliares
            temp_actual = temp 
            temperaturas = temp_list
            # Actualizar pantalla
            texto = f"Temperatura:\n[{temp_actual} °C]" if temp_actual is not None else "Esperando datos..." #Salida
            boton = Boton((0, 0, WIDTH, HEIGHT), (0, 0, 0), texto, (255, 255, 255)) #  Crea botón
            boton.dibuja()
            display.image(Boton.imagen)
            #print(f"Actualizando: {texto}")
    
    # Iniciar hilo para Bluetooth
    thread = threading.Thread(target=update_temperature, daemon=True) #Creación de hilo update_temperature, y se asegura que termine cuando finaliza el programa.
    thread.start()
    
    # Dibujando botones
    boton = Boton((0, 0, WIDTH, HEIGHT), (0, 0, 0), "Esperando datos...", (255, 255, 255))
    boton.dibuja()
    display.image(Boton.imagen)
    
    # Ejecutando y retornando
    while True:
        if touch.is_pressed():
            try:
                x_inv, y = touch.get_coordinates()
                x = WIDTH - x_inv
                print(f"Toque detectado: ({x}, {y})")
                estado = 0  # Volver al menú principal
                break
            except:
                continue
    return estado
