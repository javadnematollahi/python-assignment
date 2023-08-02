def triangle():
    triangle_check=None
    try:
        a=float(input("Enter the length of first side:\n"))
        b=float(input("Enter the length of second side:\n"))
        c=float(input("Enter the length of third side:\n"))
        if a<b+c and b<a+c and c<a+b:
            print("These three numbers could make a triangle")
        else:
            print("These three numbers could not make a triangle")
    except:
        print("your input is not valid")

triangle()