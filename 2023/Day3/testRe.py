import re

line = "2.2......12."

numbers = re.findall("\d+", line)
print(numbers)
copyLine = line
for number in numbers:
    print(copyLine)
    xpos = copyLine.find(number)
    print(number, xpos)
    copyLine = copyLine.replace(number, "." * len(number), 1)
