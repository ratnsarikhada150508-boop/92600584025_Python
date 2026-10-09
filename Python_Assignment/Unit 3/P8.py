
import re

text = "My name is Rahul and my age is 20."

pattern = "Rahul"

result = re.findall(pattern, text)

print("Text:", text)
print("Matched pattern:", result)
