
import re

file = open("data.txt", "r")
text = file.read()
file.close()

emails = re.findall(r'\S+@\S+', text)

print("Email addresses:")
for email in emails:
    print(email)
