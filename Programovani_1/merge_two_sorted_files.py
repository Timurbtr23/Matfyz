import sys


def quick_sort(array, low, high, x):

    def partition(array, low, high, x):
        pivot = array[high]

        i = low - 1

        for j in range(low, high):
            if x:
                if array[j].lower() <= pivot.lower():
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            else:
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    if low < high:

        pi = partition(array, low, high, x)

        quick_sort(array, low, pi - 1, x)
        quick_sort(array, pi + 1, high, x)


words = []

if sys.argv[1] == "-i":
    i = 2
    x = True
else:
    i = 1
    x = False

with open(sys.argv[i], 'r', encoding="utf-8") as file1:
    line = file1.readline()
    while line:
        if "\n" not in line:
            line += "\n"
        words.append(line)
        line = file1.readline()

with open(sys.argv[i+1], 'r', encoding="utf-8") as file2:
    line = file2.readline()
    while line:
        if "\n" not in line:
            line += "\n"
        words.append(line)
        line = file2.readline()

quick_sort(words, 0, len(words)-1, x)
words[-1] = words[-1][:-1]

with open(sys.argv[i+2], 'w', encoding="utf-8") as file3:
    for element in words:
        file3.write(element)
