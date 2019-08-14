"""
Mostrar el mensaje Hola NOMBRE! en el navegador accediendo a la url
http://localhost:8000/hola/NOMBRE
"""
from bottle import route, run, template

@route("/hola/<nombre>")
def index(nombre):
    """
    Función o vista que atiende las peticiones de la ruta
    """
    return template("<h3>Hola {{nombre}}!</h3>", nombre=nombre)

run(host="localhost", port=8080, reloader=True)