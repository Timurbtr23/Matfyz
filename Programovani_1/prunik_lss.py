class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False


def input_data():
    lss = LinkedList()
    temp = lss.head
    r = input()
    while r != "":
        line = r.split()
        if len(line) == 0:  # bcz the test r!="" in RCDX neukoncil cyklus!
            break
        for data in line:
            element = Node(int(data))
            if lss.head is None:
                lss.head = element
            else:
                temp.next = element
            temp = element
        r = input()
    return lss


def print_lss(lss):
    print("LSS:", end=" ")
    temp = lss.head
    while temp:
        print(str(temp.data), end=" ")
        temp = temp.next
    print('.')


def intersection(lss_1, lss_2):
    intersection_lss = LinkedList()
    temp = intersection_lss.head

    element = lss_1.head
    while element is not None:
        if intersection_lss.search(element):
            continue
        else:
            if lss_2.search(element.data):
                if intersection_lss.head is None:
                    intersection_lss.head = element
                else:
                    temp.next = element
                temp = element
        element = element.next
    if temp is not None:
        temp.next = None
    return intersection_lss


print_lss(intersection(input_data(), input_data()))
