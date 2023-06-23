list1=[1,4,3,4,1]
list2=[1,2,3]
list3=[5,9,9,5]
list4=['a','b',3,3,'b','a']
list5=[list1,list2,list3,list4]

for num,i in enumerate(list5):
    for j in range(len(i)//2):
        if i[j]!=i[len(i)-1-j]:
            print(f"list{num+1}: Nonsymmetric")
            break
    else:
         print(f"list{num+1}: symmetric")
