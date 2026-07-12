"""
AP09 Play Game - Ejercicio principal.

Construye un rectángulo a partir del ancho y alto recibidos
como argumentos desde la línea de comandos.
"""

import sys


def rectangle(width, height):
    """
    Imprime un rectángulo utilizando:

    - 'o' para las esquinas.
    - '-' para los bordes horizontales.
    - '|' para los bordes verticales.
    - Espacios para el interior.

    No imprime nada cuando el ancho o el alto es menor que uno.
    """

    # Finaliza la función cuando alguna dimensión no permite
    # construir un rectangulo valido.
    if width < 1 or height < 1:
        return

    # Cada iteracion construye una fila completa del rectangulo.
    for row in range(height):

        # La primera y la última fila corresponden a los bordes horizontales.
        is_horizontal_border = row == 0 or row == height - 1

        if is_horizontal_border:

            # Cuando el ancho es uno solo existe una posicion para la esquina.
            if width == 1:
                print("o")
            else:
                print("o" + "-" * (width - 2) + "o")

        else:

            # Para un ancho igual a uno, la fila interior contiene
            # únicamente el borde vertical.
            if width == 1:
                print("|")
            else:
                print("|" + " " * (width - 2) + "|")


def main():
    if len(sys.argv) == 3:
        try:
            x = int(sys.argv[1])
            y = int(sys.argv[2])
            rectangle(x, y)
        except ValueError:
            print("Los argumentos deben ser números enteros")
    else:
        print("Uso: python main.py <ancho> <alto>")


if __name__ == "__main__":
    main()