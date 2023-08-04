
user_list=[]
while True:
    user_input=input(f"Please enter {len(user_list)}th member of list or type 'act' to invert list:\n")
    if user_input=="act":
        user_list.reverse()
        print(user_list)
        break
    else:
        user_list.append(user_input)




