class Element:

    def __init__(self, name, data):
        self.name = name
        self.data = int(data)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i].data < arr[l].data:
        largest = l

    if r < n and arr[largest].data < arr[r].data:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, 0)


def insert(array, new_num):
    size = len(array)
    if size == 0:
        array.append(new_num)
    else:
        array.append(new_num)
        size = len(array)
        for j in range(size):
            heapify(array, size, j)


def delete_node(array):
    size = len(array)

    array[0], array[size - 1] = array[size - 1], array[0]
    deq = array.pop()

    for k in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), k)

    return deq


arr = []

while (i := input()) != "DONE":
    line = i.split()
    if line[0] == "ENQUEUE":
        insert(arr, Element(line[1], line[2]))
    if line[0] == "DEQUEUE":
        res = delete_node(arr)
        print(f'{res.name} {res.data}')

