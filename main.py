from random import randint
from art import logo

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
#Function To check users guess again actual answer
def check_answer(guess,answer,turns):
  """Check answer against guess. returns the number turns remaining"""
  if guess>answer:
    print("Too high.")
    return turns-1
  elif guess<answer:
    print("Too Low")
    return turns-1
  else:
   print(f"You got it! The answer was {answer}.")

#Make Function to set defficuty
def set_difficulty():
  level=input("Choose a difficulty. Type 'easy''hard':")
  if level=="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  #Chossing a random number between 1 and 100
  print(logo)
  print("Welcome to the Guessing Game!")
  print("I Am thinking of a number between 1 and 100.")
  answer = randint(1,100)
  print(f"Psss,the correct answer is {answer}")
  turns=set_difficulty()
  
  
  
  guess=0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
  #let the user guess number 
    guess= int(input("Make a Guess: "))
    turns =check_answer(guess, answer, turns)
    if turns==0:
      print("You have run out of guesses, You Lose.")
      return
    elif guess != answer:
      print("Guess Again.")

game()