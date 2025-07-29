from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import pymysql
import pymysql.cursors
import re
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure server-side session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'session_data')
os.makedirs(app.config['SESSION_FILE_DIR'], exist_ok=True)
Session(app)

# MySQL connection setup
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',  # or your MySQL user
        password='SW2003@th#7',  # replace with your actual password
        database='quiz_app',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks WHERE username = %s', (session['username'],))
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('home.html', username=session['username'], tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if user:
            session['username'] = user['username']
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username or password!'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Username already exists!'
        elif not re.match(r'^[A-Za-z0-9]+$', username):
            msg = 'Username must contain only letters and numbers!'
        else:
            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            connection.commit()
            msg = 'Registration successful!'
        cursor.close()
        connection.close()
    return render_template('register.html', msg=msg)

@app.route('/add', methods=['POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('login'))

    task = request.form['task']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tasks (username, task) VALUES (%s, %s)', (session['username'], task))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('home'))

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s AND username = %s', (task_id, session['username']))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)