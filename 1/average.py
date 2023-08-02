def student_level():
    name=input("Please Enter name:\n")
    lastname=input("Please Enter last name:\n")
    try:
        num1=float(input("Please Enter first number:\n"))
        num2=float(input("Please Enter second number:\n"))
        num3=float(input("Please Enter third number:\n"))
        if 0<=num1<25 and 0<=num2<25 and 0<=num3<25:
            avg=(num1+num2+num3)/3
            if 0<=avg<12:
                print(f"{name} {lastname} is Fail")
            elif 12<=avg<17:
                print(f"{name} {lastname} is Normal")
            elif 17<=avg<25:
                print(f"{name} {lastname} is Great")
        else:
            print("Inputs are out of range.")
    except:
        print("input number is not valid.")


student_level()