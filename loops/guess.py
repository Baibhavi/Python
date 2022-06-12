'''Write a Python program to guess a number between 1 and 9. User is prompted to enter a guess. If the 
user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user 
will get a "Well guessed!" message, and the program will exit.'''
import random
chosen=random.randint(1,9)
guess=0
while chosen!=guess:
    guess=int(input("Guess a number between 1 to 9 until it get right\n"))
print("Well guessed!")    
