import ctypes

def obtener_sensibilidad_actual():
    user32 = ctypes.windll.user32
    current_sensitivity = user32.SystemParametersInfoW(113, 0, None, 0)
    return current_sensitivity

def cambiar_sensibilidad(nueva_sensibilidad):
    user32 = ctypes.windll.user32
    user32.SystemParametersInfoW(113, 0, nueva_sensibilidad, 0)
    print("La sensibilidad del ratón se ha cambiado a", nueva_sensibilidad)

def main():
    print("La sensibilidad actual del ratón es:", obtener_sensibilidad_actual())
    print()

    while True:
        nueva_sensibilidad = input("Ingrese un número entre 0 y 20 para establecer la sensibilidad del ratón (o 'q' para salir): ")
        if nueva_sensibilidad.lower() == 'q':
            break

        try:
            nueva_sensibilidad = int(nueva_sensibilidad)
            if 0 <= nueva_sensibilidad <= 20:
                cambiar_sensibilidad(nueva_sensibilidad)
            else:
                print("El número ingresado está fuera del rango válido (0-20).")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

if __name__ == '__main__':
    main()
