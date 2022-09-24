import re

data = re.split(r"(\s+)", input())
w = int(input())

j = 0
for element in data:
    if len(element) > w - j:
        print()
        j = 0
    for letter in element:
        print(letter, end="")
        j += 1
        if j == w:
            j = 0
            print()
