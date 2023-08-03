


try:
    n=int(input("Enter the length of snake:\n"))
except:
    print("Input is invalid.")

for i in range(n):
    if i%2==0:
        print("*",end="")
    else:
        print("#",end="")