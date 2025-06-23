from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'students.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            gender TEXT,
            dob TEXT,
            address TEXT,
            course TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('form.html', students=students)

@app.route('/register', methods=['POST'])
def register():
    data = (
        request.form['name'],
        request.form['email'],
        request.form['phone'],
        request.form['gender'],
        request.form['dob'],
        request.form['address'],
        request.form['course']
    )

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, email, phone, gender, dob, address, course)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)