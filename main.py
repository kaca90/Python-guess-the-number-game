#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
print(logo)

print("Welcome to the number Guesing Game! The main task is to choose a number between 1 and 100.")
difficulty = input("Choose a difficulty. 'easy' or 'hard'? ")

# Easy mode
def easy_mode():
  print("You have 10 guesses.")
  number = random.randint(1, 100)
  for turn in range(1, 11):
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
    elif guess < number:
      print("Too low.")
    else:
      print(f"You got it! The number was {number}.")
      return
  print(f"You ran out of turns. The number was {number}.")

# Hard mode
def hard_mode():
  print("You have 5 guesses.")
  number = random.randint(1, 100)
  for turn in range(1, 6):
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
    elif guess < number:
      print("Too low.")
    else:
      print(f"You got it! The number was {number}.")
      return
  print(f"You ran out of turns. The number was {number}.")

# Call the appropriate function based on the difficulty chosen
def choose_difficulty(difficulty):
  if difficulty == "easy":
    easy_mode()
  elif difficulty == "hard":
    hard_mode()
  else:
    print(f"Sorry, {difficulty} is not a valid input. You need to type 'easy' or 'hard'. ")    
choose_difficulty(difficulty)

while difficulty != "easy" or difficulty != "hard":
  difficulty = input("Choose a difficulty. 'easy' or 'hard'? ")
  choose_difficulty(difficulty)