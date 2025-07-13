# A list of Quiz questions and Answers with options
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

# 15 seconds time for each question


def run_quiz():
    print("\n Welcome to the Quiz Game! \n")
    score = 0
# looping through each question
    for i, q in enumerate(quiz):
        print(f"Q{i+1}: {q['question']}")
        for option in q["options"]:  #looping through options
            print(option)

        # user answer
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! The correct answer is {q['answer']}.\n")

    print(f" Your final score: {score} out of {len(quiz)}") #users score out of 10 questions
    # Feedback messages based on the users performance
    if score == len(quiz):
        print(" Excellent! You got all right!")
    elif score >= 7:
        print(" Great job!")
    elif score >= 5:
        print(" Good attempt!")
    else:
        print(" Keep learning, Boss. You got this!")

# calling the function
run_quiz()
