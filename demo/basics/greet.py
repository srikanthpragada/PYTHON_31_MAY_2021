

hour = int(input("Enter hour of the day :"))

if hour < 12:
    message = "Good Morning"
elif hour < 17:
    message = "Good Afternoon"
else:
    message = "Good Evening"

print(message)



