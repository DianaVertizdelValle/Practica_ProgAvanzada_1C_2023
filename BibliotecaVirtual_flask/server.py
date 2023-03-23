from flask import Flask, render_template, request
from modules.archivos import cargar_lista_desde_archivo, guardar_libro_en_archivo

app = Flask(__name__)
lista_libros = []
RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos1.txt"

try:
    cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
except FileNotFoundError:
    with open(ARCHIVO, "w") as archi:
        pass
        

@app.route("/", methods=['GET', 'POST'])
def raiz():
    if request.method == 'POST':
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        puntaje = request.form["puntaje"]
        libro = {
            "nombre": titulo,
            "autor": autor,
            "puntaje": puntaje
        }
        lista_libros.append(libro)
        guardar_libro_en_archivo(ARCHIVO, libro)
    
    if len(lista_libros) == 0:
        return render_template("home.html", esta_vacia=True)
    return render_template("home.html", esta_vacia=False, lista_libros=lista_libros )

    

@app.route("/add")
def agregar():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)