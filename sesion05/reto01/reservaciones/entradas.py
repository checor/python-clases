"""Módulo con entradas para realizar un apartado."""

def requiere_apartado():
    """Pide entrada al usuario para saber si desea conocer su apartado. Repite si es necesario."""
    while True:
        apartado = input("Desea conocer el apartado (si/no)?") 
        if len(apartado) == 0:
            print("Entrada inválida. Responda si o no.")
        elif apartado[0] == 'S' or apartado[0] == 's':
            return True
        elif apartado[0] == 'N' or apartado[0] == 'n':
            return False
        else:
            print("Entrada inválida. Responda si o no.")