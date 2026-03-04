# ============================================================
# Python Basics — Ayaan's Learning Script
# Topics: Variables, Loops, Functions, Number Guessing Game
# Run with: python hello.py
# ============================================================

# -------------------------------------------------------
# 1. VARIABLES & DATA TYPES
# -------------------------------------------------------

# A variable stores a value. Python figures out the type automatically!
name = "Ayaan"         # str  (text/string)
age = 18               # int  (whole number)
gpa = 3.8              # float (decimal number)
is_student = True      # bool (True or False)

# Print: the built-in way to show output
print("Hello, World! 🌍")
print(f"My name is {name} and I am {age} years old.")  # f-string

# -------------------------------------------------------
# 2. USER INPUT
# -------------------------------------------------------

# input() reads text from the user
# We wrap it in a function so the guessing game can use it

def get_user_name():
    """Ask the user for their name and greet them."""
    user = input("What's your name? ")
    print(f"Welcome, {user}! Let's learn Python together. 🐍\n")
    return user

# -------------------------------------------------------
# 3. CONDITIONALS (if / elif / else)
# -------------------------------------------------------

def check_grade(score):
    """Return a letter grade based on score."""
    if score >= 90:
        return "A 🌟"
    elif score >= 75:
        return "B 👍"
    elif score >= 60:
        return "C 😊"
    else:
        return "F — keep studying! 💪"

# -------------------------------------------------------
# 4. LOOPS
# -------------------------------------------------------

def demonstrate_loops():
    """Show how for and while loops work."""
    print("--- For Loop: Counting 1 to 5 ---")
    for i in range(1, 6):         # range(start, stop) — stop is exclusive
        print(f"  Count: {i}")

    print("\n--- While Loop: Countdown from 3 ---")
    countdown = 3
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1            # Same as: countdown = countdown - 1
    print("  🚀 Go!\n")

    print("--- Looping through a list ---")
    topics = ["Variables", "Loops", "Functions", "OOP"]
    for index, topic in enumerate(topics, start=1):
        print(f"  {index}. {topic}")
    print()

# -------------------------------------------------------
# 5. FUNCTIONS
# -------------------------------------------------------

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def is_even(number):
    """Return True if a number is even, False if odd."""
    return number % 2 == 0

def greet(person_name, language="Python"):
    """Greet a person learning a programming language."""
    return f"Hey {person_name}, happy learning {language}!"

# -------------------------------------------------------
# 6. LISTS (Python's dynamic array)
# -------------------------------------------------------

def demonstrate_lists():
    """Show basic list operations."""
    fruits = ["apple", "banana", "cherry"]

    fruits.append("mango")      # Add to end
    fruits.insert(0, "kiwi")    # Add at index 0
    fruits.remove("banana")     # Remove by value

    print("Fruits:", fruits)
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])
    print("Number of fruits:", len(fruits))

    # List comprehension (Pythonic way to create lists)
    squares = [x ** 2 for x in range(1, 6)]
    print("Squares:", squares)
    print()

# -------------------------------------------------------
# 7. NUMBER GUESSING GAME 🎮
# -------------------------------------------------------

import random

def number_guessing_game():
    """
    A simple number guessing game.
    The computer picks a number between 1 and 20.
    The player has 5 attempts to guess it.
    """
    print("=" * 40)
    print("🎮  NUMBER GUESSING GAME")
    print("=" * 40)
    print("I'm thinking of a number between 1 and 20.")
    print("You have 5 attempts. Good luck!\n")

    secret_number = random.randint(1, 20)  # Random number 1–20
    max_attempts = 5
    attempts_used = 0
    won = False

    while attempts_used < max_attempts:
        attempts_left = max_attempts - attempts_used

        try:
            guess = int(input(f"Attempt {attempts_used + 1}/{max_attempts} — Enter your guess: "))
        except ValueError:
            print("  ⚠️  Please enter a whole number!\n")
            continue

        attempts_used += 1

        if guess == secret_number:
            print(f"\n🎉 Correct! The number was {secret_number}!")
            print(f"You got it in {attempts_used} attempt(s)! 🏆")
            won = True
            break
        elif guess < secret_number:
            print(f"  📈 Too low! Try higher. ({attempts_left - 1} attempts left)\n")
        else:
            print(f"  📉 Too high! Try lower. ({attempts_left - 1} attempts left)\n")

    if not won:
        print(f"\n😢 Game over! The number was {secret_number}. Better luck next time!")

    print("\nThanks for playing! 🐍")

# -------------------------------------------------------
# 8. MAIN — Entry point
# -------------------------------------------------------

def main():
    """Run all demonstrations and the guessing game."""
    print("=" * 40)
    print("🐍  PYTHON BASICS — by Ayaan")
    print("=" * 40 + "\n")

    # Variables demo
    print(f"Name: {name}, Age: {age}, GPA: {gpa}")
    print(f"Is student: {is_student}\n")

    # Grades demo
    print("--- Grade Checker ---")
    for score in [95, 80, 65, 45]:
        print(f"  Score {score}: Grade {check_grade(score)}")
    print()

    # Loops demo
    demonstrate_loops()

    # Lists demo
    demonstrate_lists()

    # Functions demo
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 7 even? {is_even(7)}")
    print(greet("Ayaan"))
    print()

    # Run the guessing game
    play = input("Want to play the Number Guessing Game? (yes/no): ").strip().lower()
    if play in ("yes", "y"):
        print()
        number_guessing_game()
    else:
        print("No problem! Come back anytime. 👋")


# This check means: only run main() if this file is run directly
# (not when it's imported as a module by another file)
if __name__ == "__main__":
    main()
