"""Módulo para imprimir tablas de multiplicar en la pantalla."""

def tabla(n):
    """Imprime la tabla N en la pantalla"""
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n * i))

if __name__ == "__main__":
    print("TABLA DE DEL 3")
    tabla(3)