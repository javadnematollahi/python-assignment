import random

try:
    n=int(input("Enter the length of array:\n"))
except:
    print("Input is invalid.")


length=0
arr=[]
while n!=len(arr):
    num=random.randint(0,100)
    if num not in arr:
        arr.append(num)
        

print(arr)

