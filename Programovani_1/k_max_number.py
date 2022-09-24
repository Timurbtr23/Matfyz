def bubble_sort(a):
    """
    Bubble sort is used if
        1. complexity does not matter
        2. short and simple code is preferred
    """
    change = len(a)-1
    while change > 0:
        steps = change
        change = 0
        for j in range(steps):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                change = j
    return a


k = int(input())
seznam = []
while (i := int(input())) != -1:
    seznam.append(i)

seznam = bubble_sort(seznam)
print(seznam[-k])
