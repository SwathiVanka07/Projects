# Project 1

## Quiz app using Tkinter 

This is a simple yet interactive quiz application built using Python's Tkinter library. It presents users with a series of multiple-choice questions, tracks their score, and displays the result at the end based on performance.

### Features
1.10 multiple-choice quiz questions

2.User-friendly interface using Tkinter

3.Immediate feedback after each question

4.Score tracking and performance summary

5.Clean and minimal layout

### Requirements

1. Make sure you installed python in your computer.
   
2. Tkinter comes pre-installed with most Python distributions. No need for extra dependencies.

    To verify if Tkinter is installed:  python -m tkinter

   If a window opens, you're good to go!

  ### ▶️ How to Run the App
  
1.Clone or download the repository.

2.Open a terminal (or command prompt) and navigate to the project directory.

3.Run the script:  python quiz_app.py

4.A GUI window will open where you can start answering quiz questions.

### 🧠 Quiz Content

1.Topics include general knowledge, science, programming, and technology.

2.Each question has four options (A-D).

3.The app evaluates your answer after each submission and gives immediate feedback.

### Customization

##### Want to add your own questions?

Modify the quiz list at the top of quiz_app.py:

quiz = [
    {
        "question": "Your new question?",
        "options": ["A. Option1", "B. Option2", "C. Option3", "D. Option4"],
        "answer": "A"
    },
    ...
]

##### Make sure:

1.options match the format "A. Text", "B. Text", etc.

2.answer matches the letter only ("A", "B", etc.)

---

# Project 2

## To do list using Tkinter

This is a simple and user-friendly To-Do List desktop application built with Python's Tkinter library. The app allows users to add, delete, save, and load tasks conveniently through a graphical interface.

### Features

1.Add tasks dynamically

2.Delete selected tasks

3.Save task list to a .txt file

4.Load tasks from a saved file

5.Clean and intuitive Tkinter GUI

### ✅ Requirements

Python 3.x

Tkinter is part of the standard Python library, so no extra installation is needed.

You can test if Tkinter is available with:   python -m tkinter

If a blank window appears, you're good to go!

### ▶️ How to Run the App
1.Download or clone this repository.

2.Open a terminal and navigate to the directory containing the script.

3.Run the application:  python todo_app.py

4.The To-Do List window will appear.

### How to Use

#### ➕ Add a Task

Type your task into the input box and click "Add Task".

#### ❌ Delete a Task

Select a task from the list and click "Delete Selected".

#### 💾 Save Tasks

Click "Save Tasks", choose a location and file name to store your to-do list in a .txt file.

#### 📂 Load Tasks

Click "Load Tasks" to import a task list from an existing .txt file.

---

# Project 3

## Weather app using Tkinter

This is a lightweight, easy-to-use desktop Weather App built using Python's Tkinter GUI library and the OpenWeatherMap API. Simply enter a city name, and the app will display the current temperature, weather condition, humidity, and wind speed.

### Features

Fetches real-time weather data

Displays:

1. 🌡️ Temperature (in °C)

2. ☁️ Weather condition

3. 💧 Humidity (%)

4. 💨 Wind speed (m/s)

5. User-friendly and responsive GUI

6. Error handling for empty input, network issues, and invalid city names

### ✅ Requirements

1.Python 3.x

2.requests library (install via pip if not already installed):  pip install requests

3.Tkinter comes built-in with standard Python installations.

### ▶️ How to Run

  1. Clone or download the repository.

  2. Replace the placeholder API key (API_KEY) in the script with your actual OpenWeatherMap API key.

  3. Run the app:

          python weather_app.py

   4. Enter a city name and click "Get Weather" to view results.


### Example Output

Weather in Rajahmundry, IN:
Temperature: 32°C
Condition: Scattered Clouds
Humidity: 58%
Wind Speed: 3.2 m/s


🔑 Get Your OpenWeatherMap API Key

1. Visit https://openweathermap.org/api

2. Create a free account

3. Navigate to the API keys section and generate your API key

4. Replace this line in weather_app.py:

           API_KEY = "your_api_key_here"
   
  ### 🧑‍💻 Author
  
Swathi Vanka

Enthusiastic Python developer exploring API integrations and desktop apps.

### 📃 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute it with attribution.


  
        
        
            






