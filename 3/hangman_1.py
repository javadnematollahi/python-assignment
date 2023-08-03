import random

word_bank=["tree","book","blue","train","fish","woman","life","freedom","iran","sky"]

user_mistakes=0

good_chars=[]
bad_chars=[]

x=random.randint(0,len(word_bank)-1)
word=word_bank[x]
len_win = len(set(word))

while user_mistakes<6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i],end=" ")
        else:
            print('-',end=" ")

    if len_win==len(good_chars):
        print("\nYou win")
        print("👏")
        break

    user_char=input("\nPlease write your guess:\n")
    user_char=user_char.lower()
    if len(user_char)==1:
        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            bad_chars.append(user_char)
            user_mistakes+=1
            print("❎")
    else:
        print('mese adam vared kon')



if user_mistakes==6:
    print("Game over ☠️")