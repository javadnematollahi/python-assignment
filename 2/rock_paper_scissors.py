import random

user_score=0
computer_score=0
try:
    goal_score=int(input("Please enter the goal score:\n"))
except:
    print("input is not valid")

while True:
    x=random.randint(1,3)

    if x==1:
        computer_choice="rock"
    elif x==2:
        computer_choice="paper"
    elif x==3:
        computer_choice="scissors"

    user_choice = input("choose rock or paper or scissors or type exit to finish.\n")
    if user_choice=="exit":
        print("Thank you for playing this game")
        break

    print("💻",computer_choice)
    print("🧞",user_choice)


    if computer_choice=="rock" and user_choice=="paper":
        user_score+=1
    elif computer_choice=="rock" and user_choice=="scissors":
        computer_score+=1
    elif computer_choice=="rock" and user_choice=="rock":
        pass
    elif computer_choice=="paper" and user_choice=="paper":
        pass
    elif computer_choice=="paper" and user_choice=="scissors":
        user_score+=1
    elif computer_choice=="paper" and user_choice=="rock":
        computer_score+=1
    elif computer_choice=="scissors" and user_choice=="paper":
        computer_score+=1
    elif computer_choice=="scissors" and user_choice=="scissors":
        pass
    elif computer_choice=="scissors" and user_choice=="rock":
        user_score+=1
    
    print(f"computer score is {computer_score}\nand user score is {user_score}.\n")

    if user_score==goal_score:
        print(f"Game is finished and user is winner.")
        break
    elif computer_score==goal_score:
        print(f"Game is finished and computer is winner.")
        break