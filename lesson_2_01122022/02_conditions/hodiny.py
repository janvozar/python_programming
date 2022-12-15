time = input("Please enter your time (format HH:MM): ")
hours = time.split(":")[0]
minutes = time.split(":")[1]

if int(hours) > 12:
    adjusted_hours = int(hours) - 12
    daytime = "PM"
elif int(hours) < 12:
    adjusted_hours = hours
    daytime = "AM"
    
print(f"Converted to english format: {adjusted_hours}:{minutes} {daytime}")