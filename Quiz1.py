# Author: [Yuchen Zhang]
# Date: 2025-04-02
# Description: A simple quiz game that asks users questions about animals and evaluates the answers.

def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:\n")

    # Questions and Answers
    questions = [
        "1. What is the largest animal on earth? a. Blue Whale, b. Mouse, c. Cat: ",
        "2. Which bird can fly backwards? a. Cuckoo, b. Eagle, c. Hummingbird: ",
        "3. What is the only mammal capable of flight? a. Bat, b. Squirrel, c. Dolphin: "
    ]
    answers = [
        "blue whale",  # Convert all answers to lowercase for consistent comparison
        "hummingbird",
        "bat"
    ]
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()  # Convert user input to lowercase
        if user_answer == answers[i]:  # Compare with lowercase answers
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answers[i].capitalize()}.\n")

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()
