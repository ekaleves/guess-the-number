#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random
from replit import clear

def guess_a_number():

    number = random.randint(1, 100)

    def make_a_guess(cont):
        """Check the answer with the guess. Cont is the chances that you have to guess"""
        while cont != 0:
            print(f"\nYou have {cont} attempts remaining to guess the number")
            guess = int(input("\nMake a guess: "))
            cont -= 1
            if number < guess:
                print("\nToo high.")
                if cont > 0:
                    print("Guess again!")
            elif number > guess:
                print("\nToo low.")
                if cont > 0:
                    print("Guess again!")
            elif number == guess:
               return print(f"You got it! The answer was {number}")
        return cont
    
    
    print(art.logo)
    print("Welcome to the Number Guessing Game!\n\nI'm thinking of a number between 1 and 100.\n")
    
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == "easy":
        cont = 10 
        loose = make_a_guess(cont)
        if loose == 0:
            print(f"\nYou've run out of guesses, you lose. The number was {number}\n")
    
           
    elif difficulty == "hard":
        cont = 5
        loose = make_a_guess(cont)
        if loose == 0:
            print(f"\nYou've run out of guesses, you lose. The number was {number}")
    
    else:
        print("\nWrong command, please type 'easy' or 'hard'")
    
    

guess_a_number()

game_again = input("\nDo you like to play again? type 'y' for yes or 'n' for no: ")

if game_again == "y":
    clear()
    guess_a_number()
elif game_again == "n":
    clear()
    print("Bye bye!")
else:
    print("Wrong command, Type 'y' for yes or 'n' for no")
    
