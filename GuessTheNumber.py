#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
logo = """
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
correctNumber = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ")

if difficulty=="easy":
    attempts = 15
elif difficulty=='medium':
    attempts = 10
else:
    attempts = 5

while attempts!=0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess<correctNumber:
        print("Too low.\nGuess again.")
        
    if guess>correctNumber:
        print("Too high.\nGuess again.")
    
    attempts -= 1

    if attempts==0:
        print(f"You've run out of guesses, you lose.\n{correctNumber} is the correct answer")

    if guess==correctNumber:
        print(f"You got it! The answer was {correctNumber}")
        attempts = 0
