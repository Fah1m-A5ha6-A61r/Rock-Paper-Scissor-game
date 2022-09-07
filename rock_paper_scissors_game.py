import random
print("Welcome to the game!")
playing = input("Do you want to play? (press 1 to play otherwise not)  ")
count = 0
user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
while playing == "1" :
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options :
        print("Invalid Entry. Try again")
        continue
    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    pc_pick = options[random_number]
    print("Computer picked",pc_pick + ".")

    if user_input == "rock" and pc_pick == "scissors":
        print("You win!")
        user_wins += 1
        
    elif user_input == "paper" and pc_pick == "rock":
        print("You win!")
        user_wins += 1
            
    elif user_input == "scissors" and pc_pick == "paper":
        print("You win!")
        user_wins += 1
        
    elif pc_pick == "rock" and user_input == "scissors":
        print("Computer win!")
        computer_wins += 1
        
    elif pc_pick == "paper" and user_input == "rock":
        print("Computer win!")
        computer_wins += 1
            
    elif pc_pick == "scissors" and user_input == "paper":
        print("Computer win!")
        computer_wins += 1
        
    else:
        print("Draw")

    count = count + 1
print("Played",count,"times")
print("You won",user_wins,"times and Computer won",computer_wins,"times")
print("Goodbye!")           