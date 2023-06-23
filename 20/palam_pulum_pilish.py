import random

equal_check=0
scores={"user":0,"computer1":0,"computer2":0}


for _ in range(5):
    user_hand=int(input(f"please enter 1 for \U0000270B and 2 for \U0001F91A\n"))
    while True:
        try:
            if user_hand!=1 and user_hand!=2:
                user_hand=int(input(f"please just enter 1 for \U0000270B and 2 for \U0001F91A\n"))
            else:
                break
        except:
            user_hand=int(input(f"please just enter 1 for \U0000270B and 2 for \U0001F91A\n"))
    computer1=random.randint(1,2)
    computer2=random.randint(1,2)
    if computer1==computer2==user_hand:
        equal_check+=1
        print(f"َAll show same sides.")
    else:
        if computer1==computer2:
            scores["user"]=scores["user"]+1
            print(f"user: {scores['user']}")
        elif computer1==user_hand:
            scores["computer2"]=scores["computer2"]+1
            print(f"computer2: {scores['computer2']}")
        elif user_hand==computer2:
            scores["computer1"]=scores["computer1"]+1
            print(f"computer1: {scores['computer1']}")

sorted =  sorted(scores.items(), key=lambda x:x[1])
if sorted[2][1]==sorted[1][1]==sorted[0][1]:
    print("The score of all players is zero.")
else:
    if sorted[2][1]==sorted[1][1]:
        print(f"winners are {sorted[2][0]} by {sorted[2][1]} score and {sorted[1][0]} by {sorted[1][1]} score.")
    else:
        print(f"winner is {sorted[2][0]} by {sorted[2][1]} score.")