# Project 1

# Flask Quiz app

This is a simple web-based quiz application built using Flask, a lightweight web framework in Python. The app displays multiple-choice questions one at a time and shows the user's final score at the end.

#### 📋 Features
  1. 10-question multiple-choice quiz

  2. Real-time score tracking using Flask session

  3. Question-by-question progression

  4. Final score summary page

  5. Simple and easy-to-modify structure

#### Requirements:

       Make sure python is installed in your computer.

       install Flask

You can install Flask using pip:

          pip install flask
          
### 📂 Project Structure

quiz-app/

│
├── app.py                  # Main application file

├── templates/

│   ├── index.html          # Home page

│   ├── question.html       # Question display page

│   └── result.html         # Final result page

└── README.md               # Project documentation

#### ▶️ Running the App

 1. Clone or download this repository.

 2.  Navigate to the project directory.

 3.  Run the Flask application:

           python app.py
           
 4. Open your browser and go to:
  
          http://127.0.0.1:5000/
 
#### 📄 Template Files:

Make sure the following HTML templates are located in a templates/ folder:

------

### index.html

<!DOCTYPE html>
<html>
<head><title>Quiz App</title></head>
<body>
    <h1>Welcome to the Quiz!</h1>
    <a href="{{ url_for('question') }}">Start Quiz</a>
</body>
</html>

-----

### question.html



<!DOCTYPE html>
<html>
<head><title>Question {{ q_num }}</title></head>
<body>
    <h2>Question {{ q_num }}:</h2>
    <p>{{ question['question'] }}</p>
    <form method="post">
        {% for option in question['options'] %}
            <input type="radio" name="answer" value="{{ option[0] }}" required> {{ option }}<br>
        {% endfor %}
        <button type="submit">Submit</button>
    </form>
</body>
</html>

----

### result.html



<!DOCTYPE html>
<html>
<head><title>Quiz Result</title></head>
<body>
    <h1>Quiz Completed!</h1>
    <p>Your Score: {{ score }} out of {{ total }}</p>
    <a href="{{ url_for('index') }}">Try Again</a>
</body>
</html>


#### 📦 Session Handling
  1. This app uses Flask's session management to:

  2. Store current question number

  3. Track the user's score

  4. Make sure to define a secret key in app.py:

           app.secret_key = 'your_secret_key'
### 🛠 Customization

You can easily modify or expand the quiz list in app.py to include more questions.

Improve the UI using Bootstrap or any other CSS framework.


--

# Project 2

## To do list using Flask

This is a simple To-Do List web application built using Flask, a lightweight web framework in Python. Users can add and remove tasks, and the task list is stored in memory using a Python list.

### 🧰 Features
Add tasks dynamically through a form

Remove tasks with a single click

Minimal and clean interface

All tasks are stored in a global list (in-memory)

Note: Data will be lost when the server restarts, since tasks are stored only in memory (not in a database).

### Requirements 

Make sure python is installed in your computer.

You can install Flask with pip:

            pip install flask

### 📂 Project Structure

flask-todo/
│

├── app.py                 # Main application script

├── templates/

│   └── index.html         # Main HTML template

└── README.md              # Documentation   

### ▶️ How to Run

1.Clone or download this repository.

2.Open a terminal and navigate to the project folder.

3.Run the Flask app:

           python app.py

4. Open your web browser and go to:

         http://127.0.0.1:5000/

   ### 📌 Notes
   
All tasks are stored in a global Python list (tasks), which resets when the app restarts.

Ideal for learning how Flask routing, forms, and templates work.


---

# Project 3

## Weather app using Flask

A simple Flask-based web application that fetches real-time weather information for any city using the OpenWeatherMap API. Users can enter a city name, and the app returns current temperature, humidity, and a short description of the weather.
         
### Features

Fetches current weather data using OpenWeatherMap

Displays:

Temperature (°C)

Humidity (%)

Weather description (e.g., Clear, Cloudy, Rainy)

Basic error handling for:

Invalid city names

API errors

Network issues

### 📁 Project Structure

flask-weather-app/
│

├── app.py                # Main application script

├── templates/

│   └── index.html        # HTML template for the user interface

└── README.md             # Project documentation

### ▶️ How to Run

1.Clone or download this repository.

2.Navigate to the project folder in your terminal.

3.Replace the API_KEY in app.py with your actual OpenWeatherMap API key:

                   API_KEY = "your_openweathermap_api_key"
4.Run the app:

           python app.py

### Error Handling

#### The app handles:

1.Invalid city names (404 error)

2.Invalid API key (401 error)

3.Network connectivity problems

4.Unexpected API response formats   

### 🔐 API Key Note

To use this app, you'll need a free API key from OpenWeatherMap. After signing up, copy the key and replace the placeholder value in your code:

                 API_KEY = "your_actual_api_key"

   ### Author

   ##### Swathi Vanka

     A Python and Flask enthusiast who enjoys building lightweight and functional web apps for learning and experimentation.



 ###  📃 License
 
This project is licensed under the MIT License.

You are free to:

✅ Use, copy, modify, and distribute this software

✅ Use it for personal, educational, or commercial purposes
