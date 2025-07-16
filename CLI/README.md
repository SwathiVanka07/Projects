# Project 1 

# Quiz app
This is a simple command-line quiz game built using Python. The game will ask you 10 multiple-choice questions from different topics such as general knowledge, technology, science, and more. It will keep track of your score and give you feedback based on how well you did.

✅ What This Game Does

     1. Asks you 10 questions, one by one

     2. Each question has 4 answer options: A, B, C, or D

     3. You type your answer (A/B/C/D) and press Enter

     4. It tells you whether you got the answer right or wrong

     5. At the end, it shows your total score

     6. Gives you a message depending on your score (like "Great job!" or "Keep learning!")

🛠 Requirements

To run this game, you need:

Python 3 installed on your computer
You can check your version by typing: python --version

▶️ How to Run the Game

 1. Save the code into a Python file. For example, you can name it: quiz_game.py
 
 2. Open a terminal or command prompt
 
 3. Navigate to the folder where you saved the file. Example:
 
                                                         cd path-to-your-folder
Run the game using:

    python quiz_game.py
Follow the instructions on the screen.

🧪 Example Question

Q1: What is the capital of India? A. Mumbai B. Delhi C. Hyderabad D. Chennai

Enter your answer (A/B/C/D): B

Correct!

📊 Score and Feedback

At the end of the game, it shows your score like this:

Your final score: 8 out of 10

Great job!

The feedback messages are:

10/10 → Excellent! You got all right!

7-9 → Great job!

5-6 → Good attempt!

Below 5 → Keep learning, Boss. You got this!




# Project 2 

# 📝 To-Do List App

A simple and interactive command-line To-Do List application written in Python. You can view, add, and remove tasks directly from the terminal.

📋 Features

  View your current tasks

  Add new tasks

  Remove completed or unwanted tasks

  Simple text-based interface

  Runs in an infinite loop until you choose to exit

🚀 Getting Started

1. Clone or Download

    git clone https://github.com/SwathiVanka07/todo-list-app.git

    cd todo-list-app
   
3. Run the App
   
     Make sure Python is installed on your system. Then run:

                      python todo.py
3. Use the App

--- To-Do List ---
1. View tasks
2. Add task
3. Remove task
4. Exit
Choose an option (1-4):
💡 Example

Choose an option (1-4): 2
Enter a new task: Finish homework
Task added.

Choose an option (1-4): 1
Your tasks:
1. Finish homework

Choose an option (1-4): 3
1. Finish homework
Enter the task number to remove: 1
Removed task: Finish homework

🧠 How It Works

Uses a simple list tasks[] to store all your tasks

Continuously prompts the user for an action until they choose to exit

Gracefully handles:

Empty task list

Invalid task number inputs

Invalid menu choices

📌 Requirements

    Python 3.x installed in your computer

   No external libraries required





# Project 3

# 🌤️ Weather Checker

A simple Python script to get the current weather for any city using the OpenWeatherMap API.

📋 Features

Fetches current weather data for a given city

Displays:

  1. Temperature (in Celsius)

  2. Humidity

  3. Weather condition description

  4. Handles common errors like:

  5. Invalid city name

  6. Invalid API key

  7. Network issues

🚀 How to Use

1. Clone or Download the Repository

   git clone https://github.com/SwathiVanka07/weather-checker.git
   cd weather-checker
   
2.  Make sure you have the requests library installed:

     pip install requests
    
4. Get an API Key

      Sign up for a free API key from OpenWeatherMap.

5. Run the Script

   python weather.py
   
Enter the name of the city when prompted.

Example Output

Enter city name: London

Weather in London:
Temperature: 18.3°C
Humidity: 72%
Condition: Light rain

🔐 Important

⚠️ Do not share your API key publicly. The API key used in this script should be replaced with your own for security and proper usage limits.

To improve security, consider storing the API key in an environment variable or a .env file.

✅ Error Handling

  1. 404 – City not found

  2. 401 – Invalid API key

  3. Network Errors – Internet connectivity issues

  4. Unexpected Response Format – Handles changes in API structure

🙋‍♂️ Author

This game was created by Swathi Vanka.

📜 License

 Free to use, share, and modify this code for learning or projects.
