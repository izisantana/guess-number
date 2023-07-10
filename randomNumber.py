# O computador vai ter um número secreto e o usuário tentará
# adivinhar esse numéro

#First things first: have the computer generate a secret number for us
# For this, we will use the lib random randint
import random
#creat the function
def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if (guess < random_number):
            print("Sorry, guess again. Too low!")
        elif (guess > random_number):
            print("Sorry, guess again. Too High!")
        else:
            print(f"YAY! Congrats, you have guessed the number {random_number} correctly")

#Computer guesses the user's secret number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while (feedback != 'c'):
        if (low != high):
            guess = random.randint(low, high)
        else:
            guess = low #could also be high, cause low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or Correct (C)?')
        if (feedback == "h"):
            high = guess - 1
        elif (feedback == "l"):
            low = guess + 1 
        else:
            print(f"YAY! Congrats, the computer have guessed your number, {guess}, correctly")            

computer_guess(15)