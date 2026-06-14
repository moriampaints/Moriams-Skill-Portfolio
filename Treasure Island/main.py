print("Welcome to Treasure Island/nYour mission is to find the treasure")
road = input("You're at a crossroad where do you want to go?\nType 'left' or 'right':\n ")
lake = input("You've come to a lake. There is an island in the middle of the lake."
             "\nType 'wait' to wait for a boat. Type 'swim' to swim across:\n")
door = input("Choose between three doors. Type 'Red', 'Yellow', or 'Blue':\n")
if road == "left":
    if lake == "wait":
        if door == "Red":
            print("Burned by fire. Game Over.")
        elif door == "Yellow":
            print("You win!")
        elif door == "Blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")