'''
Programa 3.- Muestra una gráfica de temperatura en °C
'''

from bluetooth_reader import read_bluetooth
import threading
from PIL import Image
import matplotlib.pyplot as plt
import io

def programa_3(display, touch, Boton):
    WIDTH, HEIGHT = display.width, display.height
    
    # Lista para almacenar datos
    temperatures = []
    
    # Función para actualizar la gráfica
    def update_graph():
        nonlocal temperatures
        for _, temp_list in read_bluetooth():
            temperatures = temp_list[-50:]  # Últimos 50 puntos para optimizar
            if temperatures:
                times, temps = zip(*temperatures)
                plt.figure(figsize=(WIDTH/100, HEIGHT/100), dpi=100)  # 240x320 píxeles
                #plt.plot([t - times[0] for t in times], temps, label="Temperatura (°C)")
                plt.xlabel("Tiempo (s)")
                plt.ylabel("Temperatura (°C)")
                plt.legend()
                plt.tight_layout()
                # Convertir gráfica a imagen PIL
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                img = Image.open(buf).resize((WIDTH, HEIGHT))
                display.image(img)
                plt.close()
                print(f"Gráfica actualizada con {len(temperatures)} puntos")
    
    # Iniciar hilo para Bluetooth
    thread = threading.Thread(target=update_graph, daemon=True)
    thread.start()
    
    # Pantalla inicial
    boton = Boton((0, 0, WIDTH, HEIGHT), (0, 0, 0), "Esperando datos...", (255, 255, 255))
    boton.dibuja()
    display.image(Boton.imagen)
    
    # Bucle para detectar toque
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
