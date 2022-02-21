"""This module does Two Things
1 => generate random number and let the user to guess it
2 => let the computer to guess the number and the user say that the guess is correct or not
"""
import random

def guess(x):
    """This Method generate Random number between 1 and X
    
    Args:
        x (int): the user input x. X is the high bound of guessing
    """    
    random_number = random.randint(1,x)
    guess = 0
    
    while guess != random_number:
        """ we will take input from the user and compare it with the random number
        
        """        
        guess = int(input(f"Guess a nubmer between 1 and {x}\n"))
        
        if guess < random_number:
            
            print("Sorry, guess again. Too low.")
        
        elif guess > random_number:
            
            print("Sorry, guess again. Too high,")
    print(f"Yeah, congrats. You have guessed the number{random_number}.")
    
    
def computer_guess(x):
    low = 1
    high = x
    
    guess = 0
    feedback = "l"
    
    
    while feedback != "c":
        
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
            
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c) ?? ")
        
        if feedback == "l":
                
            low = guess + 1
            guess = random.randint(low, high)
            
        elif feedback == "h":
            
            high = guess - 1
    
    print(f"Yay! The computer guessed your number, {guess}, correctly!")


# guess(10)
# computer_guess(10)