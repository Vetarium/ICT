totalSeconds = int(input("Please enter a number of seconds:"))

days = int(totalSeconds / 60 / 60 / 24)
totalSeconds -= days * 60 * 60 * 24

hours = int(totalSeconds / 60 / 60)
totalSeconds -= hours * 60 * 60

minutes = int(totalSeconds / 60)
totalSeconds -= minutes * 60

seconds = totalSeconds

print("The duration is: ", days,"days", hours,"hours",  minutes, "minute", seconds, "seconds")