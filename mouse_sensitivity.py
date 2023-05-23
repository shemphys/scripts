# pip install colorama
# ctypes belongs to standar python lib

import ctypes
from colorama import init, Fore, Style

#No soy capaz de que coja bien la sensibilidad inicial del mouse...
'''def obtener_sensibilidad_actual():
    user32 = ctypes.windll.user32
    current_sensitivity = user32.SystemParametersInfoW(113, 0, None, 0)
    return current_sensitivity'''

def cambiar_sensibilidad(nueva_sensibilidad):
    user32 = ctypes.windll.user32
    user32.SystemParametersInfoW(113, 0, nueva_sensibilidad, 0)
    print("La sensibilidad del ratón se ha cambiado a", nueva_sensibilidad)

def main():
    init()  # Inicializar colorama
    #print(Fore.RED + "La sensibilidad actual del ratón es:", obtener_sensibilidad_actual())
    print(Style.RESET_ALL)  # Restablecer el color al predeterminado

    while True:
        print(Fore.RED + "Miguel usa una sensibilidad de 3", Style.RESET_ALL)
        print(Fore.BLUE + "Menci usa una sensibilidad de 300", Style.RESET_ALL)
        nueva_sensibilidad = input("Ingrese un número entre 0 y 20 para establecer la sensibilidad del ratón (o 'q' para salir): ")
        if nueva_sensibilidad.lower() == 'q':
            break

        try:
            nueva_sensibilidad = int(nueva_sensibilidad)
            if 0 <= nueva_sensibilidad <= 20:
                cambiar_sensibilidad(nueva_sensibilidad)
            else:
                print("El número ingresado está fuera del rango válido (0-20).\n")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.\n")

if __name__ == '__main__':
    main()
