
nums=[]
maghsom1=[]
maghsom2=[]
moshtarak=[]
while len(nums)!=2:
    try:
        n=int(input(f"Enter {len(nums)+1}th number:\n"))
        nums.append(n)
    except:
        print("Input is invalid.")


for i in range(2):
    for j in range(1,nums[i]+1):
        if nums[i]%j==0:
            if i==0:
                maghsom1.append(j)
            elif i==1:
                maghsom2.append(j)

maghsom1.sort()
maghsom2.sort()

if len(maghsom1)>len(maghsom2):
    for i in range(len(maghsom2)):
        if maghsom2[-1-i] in maghsom1:
            print(f"Greatest common divisor is {maghsom2[-1-i]}")
            break
    else:
        print(f"{nums[0]} and {nums[1]} have not Greatest common divisor.")
else:
    for i in range(len(maghsom1)):
        if maghsom1[-1-i] in maghsom2:
            print(f"Greatest common divisor is {maghsom1[-1-i]}")
            break
    else:
        print(f"{nums[0]} and {nums[1]} have not Greatest common divisor.")





    