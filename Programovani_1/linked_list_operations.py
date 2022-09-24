class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def print_ll(self):
        if self.head is None:
            print("PRAZDNY")
        else:
            temp = self.head
            while temp:
                print(str(temp.item) + " ", end="")
                temp = temp.next
        print()

    def build(self):
        self.length = int(input())
        data = input()
        for i in range(self.length):
            self.insert_at_end(int(data.split()[i]))

    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def del_max(self):
        curr = self.head
        pos = 0
        max_data = curr.item
        while True:
            if curr.next is None:
                self.delete_node(maximum)
                return
            else:
                if curr.item > max_data:
                    maximum = pos
                    max_data = curr.item
                curr = curr.next
                pos += 1

    def delete_node(self, position):
        if self.head is None:
            return

        temp = self.head
        if position == 0:
            self.head = temp.next
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        temp = self.head
        subll = LinkedList()
        while temp is not None:
            subll.insert_at_beginning(temp.item)
            temp = temp.next
        return subll

    def del_all(self, x):
        current = self.head
        pos = 0
        while current is not None:
            if current.item == x:
                self.delete_node(pos)
                pos -= 1
            current = current.next
            pos += 1

    def find_last(self):
        temp = self.head
        count = 0
        while True:
            if temp.next is None:
                return count
            else:
                temp = temp.next
                count += 1

    def del_last_two(self):
        self.delete_node(self.find_last())
        self.delete_node(self.find_last())

    def del_even(self):
        count = 1
        curr = self.head
        while curr is not None:
            if count > 1:
                self.delete_node(count-1)
                count += 1
                curr = curr.next
            else:
                count += 1
                curr = curr.next

    def make_copy(self):
        temp = self.head
        temp2 = self.head
        count = 0
        while True:
            if temp.next is None:
                for i in range(count+1):
                    self.insert_at_end(temp2.item)
                    temp2 = temp2.next
                return
            temp = temp.next
            count += 1


if __name__ == "__main__":
    llist = LinkedList()
    llist.build()
    llist.print_ll()
    llist.del_max()
    llist.print_ll()
    llist = llist.reverse()
    llist.print_ll()
    llist.del_all(30)
    llist.print_ll()
    llist.insert_at_end(50)
    llist.print_ll()
    llist.del_last_two()
    llist.print_ll()
    llist.del_even()
    llist.print_ll()
    llist.make_copy()
    llist.print_ll()
