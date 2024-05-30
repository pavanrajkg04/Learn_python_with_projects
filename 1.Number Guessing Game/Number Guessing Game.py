# This is a placeholder file for Number Guessing Game
''' 
Q: I would like you to write a simple number guessing game in python. 
    > the game should generate a random number between 1 and 100, 
    > and the player has upto 10 attempts 
    > after each guess the game should inform the player that the number is too high or low or correct
    > if the player finishes it within 10 attempts the game should congratulate him 
    > if player exceeds 10 attempts then the game should reveal the correct number and feel sorry for him.
    > How would you approch this problem ??? 
    Come lets solve it together 
'''                                           
# first we need to import python package Random
import random 

#we start creating a function 
def Number_guessing_game():
    #we create a variable to store the random number using random ranging from 1 to 100 
    secret_number = random.randint(1,100)
    #we initialize the attempts 
    attempts = 0
    
    print("welcome to the game!")
    print("lets begin... guess the correct number that is in my mind and you have only 10 attempts")
    
    #entering a while loop as the attempt is 0 and we exit the loop if it crosses 10 attempts or we win
    while attempts < 10:
    #lets use a try catch method as we might get a string as input 
        try:
            guess = int(input("Whats your guess: "))
            attempts = attempts+1
            
            if guess == secret_number:
                print(f"congrats you guessed the number rite in {attempts} attempts")
            elif guess < secret_number:
                print("Too Low")
            else:
                print("Too High")
        except ValueError:
            print("please enter a valid number")
    if attempts == 10:
        print(f"Sorry you loose the rite number was {secret_number}")

#call the game function
Number_guessing_game()