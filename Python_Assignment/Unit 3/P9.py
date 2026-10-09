
import re

text = "Python is easy. Python is powerful."

print("Match:", re.match("Python", text))
print("Search:", re.search("easy", text).group())
print("Findall:", re.findall("Python", text))
