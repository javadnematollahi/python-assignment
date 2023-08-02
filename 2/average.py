



counter=0
avg=0
exit=True

name=input("Please Enter name and last name of student or type exit to finish:\n")
if name=="exit":
    print('goodbye')
    exit=False



while exit==True:  
    try:
        num1=input(f"Please Enter {counter+1}th grade or type exit to finish:\n")
        if num1=="exit":
            avg=avg/counter
            if 0<=avg<12:
                print(f"{name} is Fail and the average is {avg}\n")
            elif 12<=avg<17:
                print(f"{name} is Normal and the average is {avg}\n")
            elif 17<=avg<25:
                print(f"{name} is Great and the average is {avg}\n")
            print('Thank you for using average program. goodbye')
            exit=False
        else:
            if 0<=float(num1)<25 :
                counter+=1
                avg+=float(num1)
            else:
                print("Inputs are out of range.\n")
    except:
        print("input number is not valid.\n")
