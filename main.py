import sqlite3
from flask import Flask, render_template



def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    peliculas = conn.execute('SELECT * FROM peliculas').fetchall()
    conn.close()
    return render_template('index.html', peliculas=peliculas)



@app.route('/xmen')
def xmen():
    conn = get_db_connection()
    xmen = conn.execute(
        "SELECT peliculas.titulo, temas.descripcion, temas.ruta_img,temas.id_pelicula FROM peliculas INNER JOIN temas ON peliculas.id=temas.id_pelicula WHERE temas.id_pelicula IN (SELECT id_pelicula from temas WHERE id_pelicula=1)").fetchall()
    conn.close()
    return render_template('xmen.html', xmen=xmen)

@app.route('/deadpool')
def deadpool():
    conn = get_db_connection()
    deadpool = conn.execute(
        "SELECT peliculas.titulo, temas.descripcion, temas.ruta_img,temas.id_pelicula FROM peliculas INNER JOIN temas ON peliculas.id=temas.id_pelicula WHERE temas.id_pelicula IN (SELECT id_pelicula from temas WHERE id_pelicula=2)").fetchall()
    conn.close()
    return render_template('deadpool.html', deadpool=deadpool)

if __name__ == '__main__':
    app.run(debug=True)
