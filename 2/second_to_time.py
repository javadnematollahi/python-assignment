
try:
    inputtime=int(input("Enter time in second:\n"))
except:
    print("Input is not valid")
hour=inputtime//3600
minute=(inputtime-(hour*3600))//60
second=inputtime%60

if hour<10:
    strhour=f"0{hour}"
else:
    strhour=f"{hour}"

if minute<10:
    strminute=f"0{minute}"
else:
    strminute=f"{minute}"

if second<10:
    strsecond=f"0{second}"
else:
    strsecond=f"{second}"
print(f"time is {strhour}:{strminute}:{strsecond}")