


def diamond():
    try:
        n=int(input("Enter rows number:\n"))
    except:
        print("Input is invalid")
    
    max_column=2*(n-1)+1


    for i in range(max_column):
        if i>=n:
            i=abs(i-n-8)
        for j in range((max_column-(2*i+1))//2):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
            if j==max_column-1:
                print()
        for j in range((max_column-(2*i+1))//2):
            if j== ((max_column-(2*i+1))//2)-1:
                print(" ")
            else:
                print(" ",end="")


    

diamond()