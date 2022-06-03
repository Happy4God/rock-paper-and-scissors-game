import random

print("The rock, paper and scissors game. Lets get started")

R = "rock"
P = "paper"
S = "scissors"
choice_list = [R, P, S]

user_input = input("Choose between R, P,S or end: ")
if user_input == "R":
    cpu_choice = random.choice(choice_list)
    print("Player(", R, ")", ":", "CPU(", cpu_choice, ")")
    if cpu_choice == R:
        print("It is a Tie")
    elif cpu_choice == P:
        print("computer win")
    elif cpu_choice == S:
        print("you win")
elif user_input == "S":
    cpu_choice = random.choice(choice_list)
    print("Player(", S, ")", ":", "CPU(", cpu_choice, ")")
    if cpu_choice == S:
        print("It is a Tie")
    elif cpu_choice == R:
        print("computer win")
    elif cpu_choice == P:
        print("You win")
elif user_input == "P":
    cpu_choice = random.choice(choice_list)
    print("Player(", P, ")", ":", "CPU(", cpu_choice, ")")
    if cpu_choice == P:
        print("It is a tie")
    elif cpu_choice == S:
        print("computer win")
    elif cpu_choice == R:
        print("you win")
elif user_input == "end":
    print("Invalid input, Game ended")

else:
    print('Thanks for stopping by')