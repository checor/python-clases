from bottle import route, run, template

@route("/tabla/<numero>")
def tabla(numero):
    try:
        numero = int(numero)
    except ValueError:
        return template("Numero no valido") 

    tabla = """
    %for i in range(1, 11):
        <p>{{numero}} x {{i}} = {{numero * i}}</p>
    %end
    """

    return template(tabla, numero=numero)

run(host="localhost", port=8080, reloader=True)