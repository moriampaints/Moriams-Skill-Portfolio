# Code for rock paper scissors visual
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Import random library to allow for randomized selection of rock, paper, or scissors by computer player
import random

#Create list to select visual for rock, paper, or scissors
picture = [rock, paper, scissors]

#Intro to game
print("Welcome to Rock, Paper, Scissors")

#Tells player to select rock, paper or scissors and creates randomization for computer 
selection = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, and Type 2 for Scissors "))
computer = random.randint(0,2)

#Creates rule to determine winner of the game
if selection == computer:
    print("It's a draw")
elif selection == 0 and computer == 1 or selection == 2 and computer == 0:
    print("The Computer won.")
else:
    print("You won!")

#Prints the game results
print(f"You chose {picture[selection]}")
print(f"Computer choose: {picture[computer]}" ) 