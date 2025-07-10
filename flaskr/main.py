from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = 'database.db'

@app.route('/')
def index():
    books = []
    try:
        con = sqlite3.connect(DATABASE)
        db_books = con.execute('SELECT * FROM books').fetchall()
        for row in db_books:
            books.append({
                'title': row[1],
                'price': row[2],
                'arrival_day': row[3]
            })
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            pass  # テーブルがない場合は空リストのまま
        else:
            raise  # その他のOperationalErrorは再スロー
    finally:
        con.close()

    return render_template(
        'index.html',
        books=books
        )

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']

    conn = sqlite3.connect(DATABASE)
    conn.execute('INSERT INTO books (title, price, arrival_day) VALUES (?, ?, ?)', 
        [title, price, arrival_day])
    conn.commit()
    conn.close()
    return redirect(url_for('index'))