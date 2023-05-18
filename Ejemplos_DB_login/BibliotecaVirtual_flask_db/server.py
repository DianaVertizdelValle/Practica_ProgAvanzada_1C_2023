from flask import render_template, request, redirect, url_for, flash
from modules.config import app, db
from modules.databases import Book

# operaciones sobre las tablas
# Book.query.all() 
# Book.query.get(id) -> filtrar por primary key
# Book.query.filter_by( nombre="...").first() -> filtrar usando una columna de la tabla
# Book.query.filter( Book.nombre == "..." and Book.autor == "...").first() -> filtrar usando expresión lógica
# Book.query.order_by(Book.nombre).all() -> ordenar por nombre del libro
# db.session.add(...)
# db.session.delete(...)
# db.session.commit()

with app.app_context(): 
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def home(): 
    
    if request.args.get('del'):
        id = request.args.get('id')
        db.session.delete(Book.query.get(id))
        db.session.commit()
        return redirect(url_for('home'))

    lista_libros = Book.query.all()
    print(lista_libros)  
    if len(lista_libros) == 0:
        return render_template("home.html", esta_vacia=True)
    
    return render_template("home.html", esta_vacia=False, lista_libros=lista_libros )

@app.route("/add", methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        if Book.query.filter_by(nombre=request.form["titulo"]).first() == None:
            libro = Book(
                nombre = request.form["titulo"],
                autor = request.form["autor"],
                puntaje = float(request.form["puntaje"])
            )
            db.session.add(libro)
            db.session.commit()
        else:
            # https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/
            flash("El libro ya está agregado a la biblioteca")
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        id = request.form['id']
        print(id)
        libro_a_editar = Book.query.get(id) 
        libro_a_editar.nombre = request.form["titulo"]
        libro_a_editar.autor = request.form["autor"]
        libro_a_editar.puntaje = float(request.form["puntaje"])
        db.session.commit()
        return redirect(url_for('home'))   
   
    id = request.args.get('id')
    libro_a_editar = Book.query.get(id)
    print(f"id: {id}") 
    return render_template("edit.html", libro=libro_a_editar)

if __name__ == "__main__":
    app.run(debug=True)