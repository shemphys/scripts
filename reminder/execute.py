import threading
import subprocess

# Función para ejecutar matrix_rain.py en un hilo
def ejecutar_matrix_rain():
#    subprocess.call(['python', 'src/matrix_rain.py'])
    subprocess.call(['python', 'src/matrixxx.py'])
# Función para ejecutar TDAH_reminder.py en un hilo
def ejecutar_TDAH_reminder():
    subprocess.call(['python', 'src/TDAH_reminder.py'])

# Crear los hilos para ejecutar los programas
hilo_matrix_rain = threading.Thread(target=ejecutar_matrix_rain)
hilo_TDAH_reminder = threading.Thread(target=ejecutar_TDAH_reminder)

# Iniciar los hilos
hilo_matrix_rain.start()
hilo_TDAH_reminder.start()

# Esperar a que los hilos terminen (esto no se ejecutará porque los programas son bucles infinitos)
hilo_matrix_rain.join()
hilo_TDAH_reminder.join()
