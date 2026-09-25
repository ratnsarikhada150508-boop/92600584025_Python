import datetime

now = datetime.datetime.now()

print("Current date and time:", now)
print("Current date:", now.date())
print("Current time:", now.time())

print("Formatted date:", now.strftime("%d-%m-%Y"))
print("Formatted time:", now.strftime("%H:%M:%S"))
