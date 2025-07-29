# Project 1

# # Flask Task Manager with Login System

This is a simple web application built with **Flask** and **MySQL** that allows users to **register, log in, add tasks, and remove tasks**. It includes user session management, form validation, and server-side session storage.

---

## 🚀 Features

- User Registration & Login with session handling
 
- Task Management (Add / Remove)
 
- Server-side sessions using `Flask-Session`
 
- MySQL database integration using `PyMySQL`
  
- Basic input validation with regex

---

## 🛠 Tech Stack

- Python 3.x
 
- Flask
 
- Flask-Session
 
- PyMySQL
 
- MySQL (Database)

---

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

#### Update your MySQL credentials in app.py:

user='root'

password='your_password'

### Run the Application

python app.py

Then open your browser and go to:

http://127.0.0.1:5000







# Project 2

##

