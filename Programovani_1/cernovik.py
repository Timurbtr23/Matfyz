from math import sqrt


def bubble_sort(a):
    change = len(a)-1
    while change > 0:
        steps = change
        change = 0
        for j in range(steps):
            if a[j][1] < a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                change = j
    return a


data = ""
with open("vstup.txt", 'r', encoding='utf8') as file:
    for line in file:
        data += line
data = data.lower()

answer = {}
for j in range(len(data)-1):
    if data[j].isalpha() and data[j+1].isalpha():
        control = data[j:j+2]
    else:
        continue
    for i in range(len(data)):
        if control == data[i:i+2]:
            if control in answer:
                answer[control] += 1
            else:
                answer[control] = 1

answer = sorted(answer.items())
answer = bubble_sort(answer)

with open("vystup.txt", 'w', encoding='utf8') as file:
    for double in answer:
        if double != answer[-1]:
            file.write(f"{double[0]} {int(sqrt(double[1]))}\n")
        else:
            file.write(f"{double[0]} {int(sqrt(double[1]))}")
