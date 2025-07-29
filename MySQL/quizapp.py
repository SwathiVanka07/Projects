from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session

# MySQL connection
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='SW2003@th#7',  # change this
        database='quiz',
        cursorclass=pymysql.cursors.DictCursor
    )

# Quiz Questions
quiz = [
    {"question": "What is the capital of India?", "options": ["A. Mumbai", "B. Delhi", "C. Hyderabad", "D. Chennai"], "answer": "B"},
    {"question": "Which programming language is known as the backbone of web development?", "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"], "answer": "C"},
    {"question": "What does CPU stand for?", "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Peripheral Unit"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"], "answer": "C"},
    {"question": "Who is the founder of Microsoft?", "options": ["A. Steve Jobs", "B. Elon Musk", "C. Mark Zuckerberg", "D. Bill Gates"], "answer": "D"},
    {"question": "What is the chemical symbol for water?", "options": ["A. H2O", "B. O2", "C. CO2", "D. HO"], "answer": "A"},
    {"question": "Which company owns Android OS?", "options": ["A. Apple", "B. Microsoft", "C. Google", "D. Samsung"], "answer": "C"},
    {"question": "Which data structure uses LIFO order?", "options": ["A. Queue", "B. Array", "C. Stack", "D. List"], "answer": "C"},
    {"question": "What does HTML stand for?", "options": ["A. Hyper Trainer Marking Language", "B. Hyper Text Markup Language", "C. High Text Markup Language", "D. Hyper Text Marketing Language"], "answer": "B"},
    {"question": "Which organ pumps blood in the human body?", "options": ["A. Liver", "B. Brain", "C. Heart", "D. Lungs"], "answer": "C"}
]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            flash("Registration successful. Please login.")
            return redirect(url_for('login'))
        except pymysql.err.IntegrityError:
            flash("Username already exists!")
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = user['username']
            session['score'] = 0
            session['q_num'] = 0
            return redirect(url_for('question'))
        else:
            flash("Invalid credentials")
    return render_template('login.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'username' not in session:
        return redirect(url_for('login'))

    q_num = session.get('q_num', 0)
    if request.method == 'POST':
        selected = request.form.get('answer')
        correct = quiz[q_num - 1]['answer']
        if selected == correct:
            session['score'] += 1

    if q_num >= len(quiz):
        return redirect(url_for('result'))

    question = quiz[q_num]
    session['q_num'] = q_num + 1
    return render_template('question.html', question=question, q_num=q_num + 1)

@app.route('/result')
def result():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('result.html', score=session.get('score', 0), total=len(quiz))

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)