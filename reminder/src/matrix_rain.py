import time
import random
import curses

# Inicia la ventana de curses
stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.curs_set(0)  # Hace invisible el cursor
stdscr.nodelay(1)  # Hace que getch no espere a que el usuario presione una tecla

# Crea algunas variables iniciales
height, width = stdscr.getmaxyx()
height -= 1
width -= 1
matrix = [''] * width
for i in range(width):
    if random.choice([True, False]):  # Aleatoriamente decide si iniciar la columna con un número o un espacio
        matrix[i] = str(random.randint(0, 9)) + ' ' * random.randint(0, height-1)
    else:
        matrix[i] = ' ' * random.randint(0, height)

try:
    while True:
        # Dibuja la matriz
        for i in range(width):
            for j in range(height):
                if j < len(matrix[i]):
                    stdscr.addch(j, i, matrix[i][j], curses.color_pair(1))
                else:
                    stdscr.addch(j, i, ' ', curses.color_pair(1))

        # Actualiza la matriz
        for i in range(width):
            matrix[i] = matrix[i][1:] + random.choice([' ', str(random.randint(0, 9))])  # Se añade un número o un espacio al final de cada cadena

        # Actualiza la ventana
        stdscr.refresh()
        time.sleep(0.1)

finally:
    # Termina el programa de manera segura
    curses.endwin()
