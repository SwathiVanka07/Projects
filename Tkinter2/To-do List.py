from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global task list
tasks = []

# displays the list of tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

    # Route to add a new task using POST method
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')     # Get the task text from the user
    if task:
        tasks.append(task)   # Add the task to the list
    return redirect(url_for('index'))   # Redirect back to the homepage

@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    if 0 <= task_id < len(tasks):   # Check if the index is valid
        tasks.pop(task_id)           # Remove the task from the list
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)      # Start the Flask development server with debug mode on

