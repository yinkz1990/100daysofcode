day = 0
hour = 0
minute = 0

seconds = int(input("Enter the time in seconds-:"))
if seconds > 0:
    day = seconds//(24*3600)
    hour = (seconds-(day*24*3600))//3600
    minute = (seconds - ((day*24*3600)+ (hour*3600)))//60
    seconds = (seconds-((day*24*3600)+ (hour*3600) + (minute*60)))
print("The time is: ", day,"DD:", hour, "HH:", minute, "MM:", seconds,"SS")