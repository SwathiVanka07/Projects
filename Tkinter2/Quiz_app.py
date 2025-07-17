import tkinter as tk
from tkinter import messagebox

# Quiz Questions and Answers
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Hyderabad", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which programming language is known as the backbone of web development?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Peripheral Unit"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Earth", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": ["A. Steve Jobs", "B. Elon Musk", "C. Mark Zuckerberg", "D. Bill Gates"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. O2", "C. CO2", "D. HO"],
        "answer": "A"
    },
    {
        "question": "Which company owns Android OS?",
        "options": ["A. Apple", "B. Microsoft", "C. Google", "D. Samsung"],
        "answer": "C"
    },
    {
        "question": "Which data structure uses LIFO order?",
        "options": ["A. Queue", "B. Array", "C. Stack", "D. List"],
        "answer": "C"
    },
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyper Trainer Marking Language", "B. Hyper Text Markup Language", "C. High Text Markup Language", "D. Hyper Text Marketing Language"],
        "answer": "B"
    },
    {
        "question": "Which organ pumps blood in the human body?",
        "options": ["A. Liver", "B. Brain", "C. Heart", "D. Lungs"],
        "answer": "C"
    }
]

# QuizApp class handles all the quiz logic and GUI
class QuizApp:
    def __init__(self, root):
        # main window
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")
        self.score = 0
        self.current_q = 0
        # Create label to display the question
        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []    # Create radio buttons for the options
        for i in range(4):
            rb = tk.Radiobutton(root, text="", font=("Arial", 14), variable=self.var, value="", anchor="w", justify="left")
            rb.pack(fill="x", padx=20, pady=5)
            self.options.append(rb)
          # Submit button to submit the selected answer
        self.submit_btn = tk.Button(root, text="Submit", command=self.submit_answer, font=("Arial", 14))
        self.submit_btn.pack(pady=20)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack()
        # Load the question
        self.load_question()

    def load_question(self):
        if self.current_q < len(quiz):
            q_data = quiz[self.current_q]
            self.question_label.config(text=f"Q{self.current_q + 1}: {q_data['question']}")
            self.var.set(None)
            for i, option in enumerate(q_data["options"]):
                self.options[i].config(text=option, value=option[0])
        else:
            self.end_quiz() # If all questions are done, show final result

    def submit_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No answer", "Please select an option.")
            return
        
            # Check if the selected answer is correct
        correct = quiz[self.current_q]["answer"]
        if selected == correct:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(
                text=f"Wrong! Correct answer was {correct}.", fg="red")

        self.current_q += 1     # Move to the next question

        self.root.after(1000, self.load_question)

    def end_quiz(self):
        self.question_label.pack_forget()
        for rb in self.options:
            rb.pack_forget()
        self.submit_btn.pack_forget()
        self.feedback_label.pack_forget()

           # Show the final score and a message based on performance
        result = f"Your score: {self.score} out of {len(quiz)}\n"
        if self.score == len(quiz):
            result += "Excellent! You got all right!"
        elif self.score >= 7:
            result += "Great job!"
        elif self.score >= 5:
            result += "Good attempt!"
        else:
            result += "Keep learning, Boss. You got this!"
         
         # Display the result message
        final_label = tk.Label(self.root, text=result, font=("Arial", 16), wraplength=500, justify="center")
        final_label.pack(pady=50)

# Run the app 
if __name__ == "__main__":
    root = tk.Tk()         # Create the main window
    app = QuizApp(root)     # Create an instance of QuizApp
    root.mainloop()         # Run the Tkinter event loop

