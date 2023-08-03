
nums=[]
maghsom1=[]
maghsom2=[]
adad=1


def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

def maghsom_prime(n):
    maghsom=[]
    for i in range(2,n+1):
        if n%i==0:
            check=prime(i)
            if check==True:
                maghsom.append(i)
    return maghsom


while len(nums)!=2:
    try:
        n=int(input(f"Enter {len(nums)+1}th number:\n"))
        nums.append(n)
    except:
        print("Input is invalid.")


maghsom1=maghsom_prime(nums[0])
maghsom2=maghsom_prime(nums[1])

    

while True:
    adad=1
    for k in maghsom1:
        adad*=k
    if adad!=nums[0]:
        new=nums[0]//adad
        maghsom1=maghsom1+maghsom_prime(new)
    else:
        break

while True:
    adad=1
    for k in maghsom2:
        adad*=k
    if adad!=nums[1]:
        new=nums[1]//adad
        maghsom2=maghsom2+maghsom_prime(new)
    else:
        break

print(maghsom2)
print(maghsom1)
final_arr=[]
for i in maghsom1:
    if i in maghsom2:
        maghsom2.remove(i)
    final_arr.append(i)
final_arr=final_arr+maghsom2
adad=1
for k in final_arr:
    adad*=k

print(f"Least Common Multiple of {nums[0]} and {nums[1]} is {adad}")

            



