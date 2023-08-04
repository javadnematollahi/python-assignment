
try:
    n=int(input("Enter a number bigger or equal to zero:"))
    if n>=0 and n<=2:
        print(f"{n} is factorial.")
    elif n>2:
        res=1
        for i in range(1,n//2+1):
            if n%i==0:
                res=res*i
                if res==n:
                    print(f"{n} is factorial.")
                    break
            else:
                print(f"{n} is not factorial.")
                break
        else:
            print(f"{n} is not factorial.")

    if n<0:
        print("Input is invalid.")
except:
    print("Input is invalid.")







