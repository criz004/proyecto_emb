import serial
import time
import re

def read_bluetooth():
    port = '/dev/rfcomm0'  # Puerto Bluetooth
    baud_rate = 9600       # Velocidad del HC-05
    temperaturas = []      # Lista para guardar temperaturas y tiempos
    
    try:
        with serial.Serial(port, baud_rate, timeout=2) as bluetooth:
            print(f"Conexión establecida :D en {port}. Recibiendo temperaturas...") 
            while True:
                if bluetooth.in_waiting > 0:  # Sí hay datos disponibles
                    try:
                        linea = bluetooth.readline().decode('utf-8').strip() #Almacena los datos como string
                        if linea and linea.split(): #Si exite el dato 
                            print(f"Dato recibido: '{linea}'")
                            match = re.match(r'(\d+\.\d{3})\s*C', linea) #Validación de la línea con una expresión regular (busqueda
                            if match: #Si tiene un formato valido
                                try: #Empieza
                                    temp = float(match.group(1)) #Lo convierte a numero flotante
                                    if 0 <= temp <= 100:  # Validar temperatura aceptable :D
                                        temperaturas.append((time.time(), temp)) # Tupla de temperaturas
                                        if len(temperaturas) > 100:  # Limitar a 100 temps en la Tupla
                                            temperaturas.pop(0) #Si sobrepasa de 100, elimina la primera y así...
                                        print(f"Valor Almacenado: {time.time()}, {temp}")
                                        yield temp, temperaturas #Devuelve tupla 
                                    else:
                                        print(f"Temperatura fuera de rango D: : {temp}")
                                except ValueError:
                                    print(f"Dato inválido :o : '{linea}'")
                            else:
                                print(f"Formato inválido :c : '{linea}'")
                    except UnicodeDecodeError:
                        print("Error de decodificación!!! D: :")
                time.sleep(0.1)  # Pausando
    except serial.SerialException as e:
        print(f"Error al acceder al puerto serie: {e}")
        return None, []
    except KeyboardInterrupt:
        print("Programa interrumpido. Cerrando conexión...")
        return None, []
    finally:
        bluetooth.close()
        print("Puerto serial cerrado")
