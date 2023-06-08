import pygame
from pymatrix_rain import MatrixRain

# Crea una instancia de la clase MatrixRain
matrix_rain = MatrixRain()

# Configura las opciones de la lluvia de la matriz
matrix_rain.set_colors((0, 255, 0), (0, 0, 0))  # Color del texto y color de fondo
matrix_rain.set_density(0.2)  # Densidad de los caracteres (0.0 a 1.0)

# Inicia la lluvia de la matriz
matrix_rain.start()
