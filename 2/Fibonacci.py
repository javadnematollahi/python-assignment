

try:
    n=int(input("Enter a number:\n"))
except:
    print("Input is invalid")

fib=[]
for i in range(n):
    if i<2:
        fib.append(1)
        print(1, end=" ")
    if i>1:
        fib.append(fib[i-2]+fib[i-1])
        print(fib[i], end=" ")


