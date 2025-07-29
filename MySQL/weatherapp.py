from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

API_KEY = "277353313a9d07cdb6a93d303dd8d52e"  # OpenWeatherMap API Key

# MySQL connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='password',  # change this to your MySQL password
        database='weather_app',
        cursorclass=pymysql.cursors.DictCursor
    )

# Get weather function
def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            "city": city_name.title(),
            "temperature": main['temp'],
            "humidity": main['humidity'],
            "description": weather['description'].capitalize()
        }
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {"error": f"City '{city_name}' not found. Please check the spelling and try again."}
        elif response.status_code == 401:
            return {"error": "Invalid API key. Please check your key."}
        else:
            return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Network error occurred: {req_err}"}
    except KeyError:
        return {"error": "Unexpected response format. Please try again later."}

# -------------------- ROUTES --------------------

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city)
    return render_template('index.html', weather=weather_data)

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
            flash('Registration successful. Please login.')
            return redirect(url_for('login'))
        except pymysql.err.IntegrityError:
            flash('Username already exists. Please choose another.')
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
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect(url_for('weather'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
