# Project 1

# # Flask Task Manager with Login System

This is a simple web application built with **Flask** and **MySQL** that allows users to **register, log in, add tasks, and remove tasks**. It includes user session management, form validation, and server-side session storage.



## 🚀 Features

- User Registration & Login with session handling
 
- Task Management (Add / Remove)
 
- Server-side sessions using `Flask-Session`
 
- MySQL database integration using `PyMySQL`
  
- Basic input validation with regex



## 🛠 Tech Stack

- Python 3.x
 
- Flask
 
- Flask-Session
 
- PyMySQL
 
- MySQL (Database)



## 📁 Project Structure

project/
│

├── app.py # Main application

├── templates/

│ ├── home.html # Dashboard page

│ ├── login.html # Login form

│ └── register.html # Registration form

├── session_data/ # Folder for storing server-side session files

### 2. Set Up Virtual Environment 

python -m venv venv

### 3. Install Dependencies

pip install Flask Flask-Session PyMySQL

### 4. Set Up MySQL Database

Open MySQL and create the database:

CREATE DATABASE quiz_app;

USE quiz_app;

CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,
    
    username VARCHAR(50) NOT NULL UNIQUE,
    
    password VARCHAR(100) NOT NULL
);

CREATE TABLE tasks (

    id INT AUTO_INCREMENT PRIMARY KEY,
    
    username VARCHAR(50) NOT NULL,
    
    task TEXT NOT NULL
);

#### Update your MySQL credentials in the code:

user='root'

password='your_password'

### Run the Application

python app.py

Then open your browser and go to:

http://127.0.0.1:5000




---


# Project 2

## Flask Quiz App with Login System

This is a simple **quiz web application** built using **Flask** and **MySQL**, where users can **register, log in, attempt a quiz**, and **view their score** at the end. It uses sessions to track user progress and flash messages for feedback.

##  Features

- 🔐 User Registration & Login
  
- 📋 Multiple-choice quiz (10 questions)
  
- ✅ Score tracking and result display
  
- 🔁 Session handling and logout
  
- ⚡ Flash messages for success/error feedback

### project/
│

├── app.py # Main application

├── templates/

│ ├── login.html # Login page

│ ├── register.html # Registration page

│ ├── question.html # Quiz question interface

│ └── result.html # Final result page

### 2. Install Dependencies

pip install Flask PyMySQL

### 3. Set Up MySQL Database

Log in to your MySQL and create the database and user table:

CREATE DATABASE quiz;

USE quiz;

CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,
    
    username VARCHAR(50) UNIQUE NOT NULL,
    
    password VARCHAR(100) NOT NULL
    
);

### Update your MySQL credentials in the code:

user='root'

password='your_mysql_password'

### Run the Application

python app.py

Then open your browser and go to:

 http://127.0.0.1:5000


 ---

 # Project

## Flask Weather App

This is a simple weather forecast web application built using Flask, with user registration/login functionality and weather data fetched from the OpenWeatherMap API.

### Features

User Registration and Login

Search weather by city name

Fetches current temperature, humidity, and description

Uses OpenWeatherMap API

Weather results shown only after login

Passwords stored directly (for demo only — hash in production)


### Project Structure

weather_app/

├── templates/

│   ├── index.html

│   ├── login.html

│   └── register.html

├── app.py




### Install requirements

pip install flask pymysql requests

#### Set up the MySQL database

CREATE DATABASE weather_app;

USE weather_app;

CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,
    
    username VARCHAR(100) UNIQUE NOT NULL,
    
    password VARCHAR(100) NOT NULL
    
);

### Update your database credentials in the code:

user='root',

password='your_mysql_password'

#### Replace API Key

Get a free API key from OpenWeatherMap and replace the value of API_KEY in app.py.

API_KEY = "your_actual_api_key"

### Run the application

python app.py

Open http://127.0.0.1:5000 in your browser.


### Security Note

1. Passwords are stored in plain text — for real apps, use hashing (e.g., werkzeug.security).

2. CSRF protection is not added — for production, use Flask-WTF or similar.

3. Do not expose your API key publicly.













 



