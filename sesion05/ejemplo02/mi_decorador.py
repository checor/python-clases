def mi_decorador(funcion):
    def nueva(*args):
        # Codigo antes del llamado
        print("Llamada a la funcion", funcion.__name__)
        retorno = funcion(*args)
        # Codigo despues del llamado
        print("La función ha sido llamada")
        return retorno + 1 # Agrega 1 al resultado de la funcion
    return nueva

@mi_decorador
def mi_funcion(numero):
    return numero * 2

print(mi_funcion(5))