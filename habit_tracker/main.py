import json
import datetime
from typing import List
from colorama import Fore, init
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

init(autoreset=True)  # Para que los colores de colorama se reseteen automáticamente

class Habilidad:
    def __init__(self, nombre: str, descripcion: str, fecha_creacion: str = None, fecha_actualizacion: str = None, racha_mas_larga: int = 0, racha_actual: int = 0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.datetime.now().isoformat()
        self.fecha_actualizacion = fecha_actualizacion if fecha_actualizacion else self.fecha_creacion
        self.racha_mas_larga = racha_mas_larga
        self.racha_actual = racha_actual
    
    def mostrar(self, index: int):
        diferencia = relativedelta(datetime.datetime.now(), parse(self.fecha_actualizacion))
        if diferencia.days == 0 and self.racha_actual > 0:  # Verifica que la habilidad ha sido trabajada hoy
            color = Fore.GREEN
        elif diferencia.days == 1 or (diferencia.days == 0 and self.racha_actual == 0):  # Verifica si la habilidad es nueva (no se ha trabajado hoy) o si no se trabajó ayer
            color = Fore.YELLOW
        else:
            color = Fore.RED

        print(f"{color}{index+1}. {self.nombre} - {self.descripcion} (Racha actual: {self.racha_actual}, Racha más larga: {self.racha_mas_larga})")
    

    def __repr__(self):
        return f"Habilidad(nombre={self.nombre}, descripcion={self.descripcion}, fecha_creacion={self.fecha_creacion}, fecha_actualizacion={self.fecha_actualizacion}, racha_mas_larga={self.racha_mas_larga}, racha_actual={self.racha_actual})"

    def actualizar(self):
        self.fecha_actualizacion = datetime.datetime.now().isoformat()
        self.racha_actual += 1
        if self.racha_actual > self.racha_mas_larga:
            self.racha_mas_larga = self.racha_actual

    def reiniciar_racha(self):
        self.racha_actual = 0

    def mostrar(self, index: int):
        diferencia = relativedelta(datetime.datetime.now(), parse(self.fecha_actualizacion))
        if diferencia.days == 0:
            color = Fore.GREEN  # Hecho hoy
        elif diferencia.days == 1:
            color = Fore.YELLOW  # No hecho hoy
        else:
            color = Fore.RED  # No hecho en 24 horas o más

        print(f"{color}{index+1}. {self.nombre} - {self.descripcion} (Racha actual: {self.racha_actual}, Racha más larga: {self.racha_mas_larga})")

class MonitorHabitos:
    # Aquí se mantiene el código previo...
    def __init__(self, filename: str = 'habilidades.json'):
        self.filename = filename
        self.habilidades = []  # Inicializa self.habilidades como una lista vacía
        try:
            self.habilidades = self.cargar_habilidades()
        except FileNotFoundError:
            pass

    def guardar_habilidades(self):
        with open(self.filename, 'w') as f:
            json.dump([ob.__dict__ for ob in self.habilidades], f)

    def agregar_habilidad(self, nombre: str, descripcion: str):
        nueva_habilidad = Habilidad(nombre, descripcion)
        self.habilidades.append(nueva_habilidad)
        self.guardar_habilidades()
        
    def cargar_habilidades(self) -> List[Habilidad]:
        with open(self.filename, 'r') as f:
            habilidades_dict = json.load(f)
        return [Habilidad(**habilidad) for habilidad in habilidades_dict]

    def mostrar_habilidades(self):
        for i, habilidad in enumerate(self.habilidades):
            habilidad.mostrar(i)

    def actualizar_habilidad(self, index: int):
        self.habilidades[index].actualizar()
        self.guardar_habilidades()

    def actualizar_descripcion(self, index: int, nueva_descripcion: str):
        self.habilidades[index].descripcion = nueva_descripcion
        self.guardar_habilidades()

    def eliminar_habilidad(self, index: int):
        del self.habilidades[index]
        self.guardar_habilidades()

# Función principal del programa
def main():
    monitor = MonitorHabitos()

    while True:
        monitor.mostrar_habilidades()

        print("\n¿Qué quieres hacer?")
        print("1. Actualizar habilidades que he hecho hoy")
        print("2. Actualizar la descripción de una habilidad")
        print("3. Añadir una nueva habilidad")
        print("4. Eliminar una habilidad")
        print("5. Salir")

        opcion = int(input("Ingresa el número de la opción que quieras: "))

        if opcion == 1:
            index = int(input("Ingresa el número de la habilidad que quieres actualizar: ")) - 1
            monitor.actualizar_habilidad(index)
        elif opcion == 2:
            index = int(input("Ingresa el número de la habilidad cuya descripción quieres actualizar: ")) - 1
            nueva_descripcion = input("Ingresa la nueva descripción: ")
            monitor.actualizar_descripcion(index, nueva_descripcion)
        elif opcion == 3:
            nombre = input("Ingresa el nombre de la nueva habilidad: ")
            descripcion = input("Ingresa la descripción de la nueva habilidad: ")
            monitor.agregar_habilidad(nombre, descripcion)
        elif opcion == 4:
            index = int(input("Ingresa el número de la habilidad que quieres eliminar: ")) - 1
            monitor.eliminar_habilidad(index)
        elif opcion == 5:
            break
        else:
            print("Opción no reconocida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
