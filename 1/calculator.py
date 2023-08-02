import math

def degree_to_rad(degree):
    radian=(degree/180)*math.pi
    return radian


while True:
    while True:
        try:
            operation=int(input("Choose the number of your desired operation: \n1. sqrt    2.sin    3.cos    4.tan    5. cot    6. factorial    \
                                \n7.log    8.sum    9.sub    10.multiplication    11.divide   12.exit\n"))
            if 0<operation<13:
                break
            else:
                print("your input is not valid.\n")
        except:
            print("your input is not valid.\n")
    try:    
        if operation>0 and operation<8:
            num1=float(input("Enter a number: \n"))
        elif operation>7 and operation<12:
            num1=float(input("Enter first number: \n"))
            num2=float(input("Enter second number: \n"))
    except:
        print("your input is not valid.\n")

    if 1<operation<6:
        num1=degree_to_rad(num1)
    
    if operation==1:
        try:
            result=math.sqrt(num1)
        except ValueError:
            result="Couldn't get a negative number"
    elif operation==2:
        result=round(math.sin(num1),2)
    elif operation==3:
        result=round(math.cos(num1),2)
    elif operation==4:
        try:
            result=math.sin(num1)/round(math.cos(num1),2)
        except ZeroDivisionError:
            result="Couldn't divid by zero"
    elif operation==5:
        try:
            result=math.cos(num1)/round(math.sin(num1),2)
        except ZeroDivisionError:
            result="Couldn't divid by zero"
    elif operation==6:
        try:
            if num1%round(num1)==0:
                num1=int(num1)
            result=math.factorial(num1)
        except:
            result="Couldn't get float or negative number"
    elif operation==7:
        try:
            result=math.log(num1)
        except ValueError:
            result="Couldn't get negative number"
    elif operation==8:
        result=num1+num2
    elif operation==9:
        result=num1-num2
    elif operation==10:
        result=num1*num2
    elif operation==11:
        try:
            result=num1/num2
        except ZeroDivisionError:
            result="Couldn't divid by zero"
    elif operation==12:
        break
    print(result)



