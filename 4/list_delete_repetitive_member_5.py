user_list=[]
output_list=[]
while True:
    user_input=input(f"Please enter {len(user_list)}th member of list or type 'act' to delete repetitive members of list:\n")
    if user_input=="act":
        print(f"Input list: {user_list}")
        # user_list=list(set(user_list))
        for i in user_list:
            if i not in output_list:
                output_list.append(i)

        print(f"Output list: {output_list}")
        break
    else:
        user_list.append(user_input)