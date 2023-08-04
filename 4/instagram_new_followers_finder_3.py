import instaloader
import getpass

print("This code find new follower of javad_nl instagram account.\n")

f= open("followers.txt","a+")
old_followers=[]
for line in f:
    old_followers.append(line)

f.close()


L = instaloader.Instaloader()

password=getpass.getpass()
L.login(user="javad_nl",passwd=password)
print("connect successfully.\n")

new_account=input("please enter the account that you want to find new followers of it:")
profile= instaloader.Profile.from_username(L.context,new_account)

new_followers=[]

for follower in profile.get_followers():
    new_followers.append(follower)

f= open('followers.txt','w')
for follower in new_followers:
    f.write(follower + "\n")

f.close()

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

