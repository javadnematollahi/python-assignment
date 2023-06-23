import random


boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']
married_list=[]
lenght_boys=list(range(0,len(boys)))
lenght_girls=list(range(0,len(boys)))

if len(boys)<len(girls):
    min_lenght=len(boys)
else:
    min_lenght=len(girls)

for i in range(min_lenght):
    a=random.choice(lenght_boys)
    b=random.choice(lenght_girls)
    married_list.append((boys[a],girls[b]))
    lenght_boys.remove(a)
    lenght_girls.remove(b)
print(married_list)
