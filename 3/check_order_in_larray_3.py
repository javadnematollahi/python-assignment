user_arr=[]

while True:
    try:
        num=input(f"Please enter {len(user_arr)}th member of array \nor type check to check to check order:")
        if num=="check":
            print(user_arr)
            for i in range(1,len(user_arr)):
                if user_arr[i-1]>user_arr[i]:
                    print("Your array is not arranged from low to high")
                    break
            else:
                print("Your array is arranged from low to high")
            break
                

        else:
            num=int(num)
            user_arr.append(num)
    except:
        print("Input is invalid, please enter a number or type check.\n")