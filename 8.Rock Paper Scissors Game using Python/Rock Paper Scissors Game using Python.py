'''
Q: You're tasked with implementing a simple Rock, Paper, Scissors game in Python. 
Your implementation should allow a player to choose their move (Rock, Paper, or Scissors) and then 
determine the winner based on the classic rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. 
Can you outline your approach to designing and coding this game, considering factors like code structure, 
user input validation, and handling game outcomes?

'''
from random import randint  # Importing the randint function from the random module
player = input("Do you want to play or quit : ").lower()  # Asking the player if they want to play or quit the game and converting their input to lowercase

def game_play(cpu,player):  # Defining a function called game_play that takes two arguments: cpu and player
    if cpu == "rock" and player == "paper":  # Checking if the CPU chose Rock and the player chose Paper
        print("Player Won")  # Printing a message indicating that the player won
    elif cpu == "paper" and player == "scissor":  # Checking if the CPU chose Paper and the player chose Scissor
        print("Player Won")  # Printing a message indicating that the player won
    elif cpu == "scissor" and player == "rock":  # Checking if the CPU chose Scissor and the player chose Rock
        print("Player Won")  # Printing a message indicating that the player won
    elif cpu == player:  # Checking if both CPU and player chose the same move
        print("Tie")  # Printing a message indicating that it's a tie
    else:  # If none of the above conditions are met, implying that the CPU won
        print("cpu Won")  # Printing a message indicating that the CPU won
    print(f"cpu choice was {cpu}")  # Printing the CPU's choice

while(player != "quit"):  # Starting a while loop that continues until the player enters "quit"
    lists = ["Rock","Paper","Sissor"]  # Creating a list containing the possible moves: Rock, Paper, and Scissor
    length = len(lists)  # Getting the length of the list
    player = input("enter your choice, (rock,paper or sissor and quit to exit the game) : ").lower()  # Asking the player to enter their choice and converting it to lowercase
    
    cpu = lists[randint(0,length-1)].lower()  # Generating a random choice for the CPU from the list of moves
    
    game_play(cpu,player)  # Calling the game_play function with the CPU's choice and the player's choice as arguments

print("Thank you for playing")  # Printing a message to thank the player for playing the game
