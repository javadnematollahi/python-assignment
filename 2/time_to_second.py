

inputtime=input("Enter time in below format to convert to second:\nhh:mm:ss\n")
arr_time=inputtime.split(":")
second=int(arr_time[0])*3600+int(arr_time[1])*60+int(arr_time[2])
print(f"{second} second.")