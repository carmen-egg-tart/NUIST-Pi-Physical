# Author: [Your Name]
# Date: 2025-04-02
# Description: A quiz game that interacts with LEDs on a Raspberry Pi using GPIO pins.

import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
RED_LED = 17  # Red LED connected to GPIO 17
GREEN_LED = 18  # Green LED connected to GPIO 18

# Set up pins as output
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

def turn_on_led(pin):
    """Turn on an LED."""
    GPIO.output(pin, GPIO.HIGH)

def turn_off_led(pin):
    """Turn off an LED."""
    GPIO.output(pin, GPIO.LOW)

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
        "blue whale",  # All answers are converted to lowercase for consistent comparison
        "hummingbird",
        "bat"
    ]
    score = 0

    # Ask questions
    for i in range(len(questions)):
        user_answer = input(questions[i]).strip().lower()  # Convert user input to lowercase
        if user_answer == answers[i]:  # Compare with lowercase answers
            print("Correct!\n")
            turn_on_led(RED_LED)  # Turn on RED LED for correct answer (Changed from GREEN to RED)
            time.sleep(1)
            turn_off_led(RED_LED)  # Turn off RED LED after 1 second
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answers[i].capitalize()}.\n")
            turn_on_led(GREEN_LED)  # Turn on GREEN LED for incorrect answer (Changed from RED to GREEN)
            time.sleep(1)
            turn_off_led(GREEN_LED)  # Turn off GREEN LED after 1 second

    # Provide final score
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")

    # Cleanup GPIO
    GPIO.cleanup()

# Run the quiz function
if __name__ == "__main__":
    quiz()
