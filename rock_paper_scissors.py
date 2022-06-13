# import random module
import random
 
# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")

play = True

while play == True:
    possible_actions = ["R", "P", "S"]
    
    # take the input from user
    user_action = input("User turn: ")
    user_action = user_action.upper()

    while(user_action not in possible_actions):
        print("Invalid choice enterred")
        print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")
        user_action = input("User turn: ").upper()
    
    computer_action = random.choice(possible_actions)
    print(f"\nPlayer ({user_action}) : CPU ({computer_action})\n")

    if(user_action == computer_action):
        print(f"Both players selected {user_action}. It's a tie!")
        play = True
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! Computer wins.")
        print("\nThanks for playing")
        play = False
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! Computer wins.")
        print("\nThanks for playing")
        play = False
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! Computer wins.")
        print("\nThanks for playing")
        play = False
    

    