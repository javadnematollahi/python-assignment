import numpy as np
import math
import cmath

def solve_cubic_equation():
    try:
        a=float(input("Please enter a:\n"))
        b=float(input("Please enter b:\n"))
        c=float(input("Please enter c:\n"))
        d=float(input("Please enter d:\n"))
    except:
        print("Input is not a number!")


    delta0=b**2-3*a*c

    delta1=2*(b**3)-9*a*b*c+27*(a**2)*b

    delta=((delta1**2)-4*(delta0**3))/(-27*(a**2))

    CC=np.cbrt((math.sqrt((delta1**2)-4*(delta0**3))+delta1)/2)

    u=[1,(-1+1j*math.sqrt(3))/2,(-1-1j*math.sqrt(3))/2]
    roots=[]
    try:
        for i in range(1,4):
            roots.append(((b+((u[i-1])*CC)+(delta0/((u[i-1])*CC)))/(-3*a)))
    except ZeroDivisionError:
        roots=[]
        for _ in range(3):
            roots.append((-b)/(3*a))
    print(roots)


solve_cubic_equation()