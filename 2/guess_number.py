import random



guess_counter=0
computer_number=random.randint(1,100)
while True:
    user_number=input("Guess a new number or type exit to finish:\n")
    if user_number=="exit":
        print("Thank you for playing this game")
        break
    else:
        user_number=int(user_number)
    guess_counter+=1

    if computer_number==user_number:
        print(f"You guess {guess_counter} times.")
        print("barikala")
        print("👏")
        break
    elif computer_number>user_number:
        print("go up")
    elif computer_number<user_number:
        print("go down")


