class Stack:
    """
    Applications of Stack Data Structure
        To reverse a word
        In compilers
        In browsers
    """

    def __init__(self):
        self.items = []
        self.top = -1

    def __str__(self):
        return f"{self.items}"

    def check_empty(self):
        return self.top == -1

    def push(self, item):
        self.items.append(item)
        self.top += 1
        print("pushed item: " + str(item))

    def pop(self):
        if self.check_empty():
            return "stack is empty"
        print("popped item: " + str(self.items[self.top]))
        del self.items[self.top]
        self.top -= 1


class Queue:
    """
    Applications of Queue
        CPU scheduling, Disk Scheduling
        When data is transferred asynchronously between two processes.The queue is used for synchronization.
        Handling of interrupts in real-time systems.
        Call Center phone systems use Queues to hold people calling them in order.
    """

    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1

    def __str__(self):
        return f"{self.queue}"

    # Add an element
    def enqueue(self, item):
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        if self.front >= self.rear:
            del self.queue[self.front]
            self.front = -1
            self.rear = -1
        else:
            del self.queue[0]
            self.front += 1

    def size(self):
        return len(self.queue)


class CircularQueue:
    """
    Applications of Circular Queue
        CPU scheduling
        Memory management
        Traffic Management
    """

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if (self.tail + 1) % self.k == self.head:
            print("The circular queue is full\n")

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
            temp = self.queue[self.head]

    def dequeue(self):
        if self.head == -1:
            print("The circular queue is empty\n")

        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k

    def __str__(self):
        if self.head == -1:
            return "No element in the circular queue"

        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


class Deque:
    """
    Applications of Deque Data Structure
        In undo operations on software.
        To store history in browsers.
        For implementing both stacks and queues.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_rear(self, item):
        self.items.append(item)

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# Linked list implementation in Python
class LinkedList:
    """
    Linked List Applications
        Dynamic memory allocation
        Implemented in stack and queue
        In undo functionality of softwares
        Hash tables, Graphs
    """

    def __init__(self):
        self.head = None

    def print_ll(self):
        temp = self.head
        while temp:
            print(str(temp.item) + " ", end="")
            temp = temp.next

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

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

    def search(self, key):
        current = self.head
        while current is not None:
            if current.item == key:
                return True
            current = current.next
        return False

    # Sort the linked list
    def sort_linked_list(self, head):
        current = head

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.item > index.item:
                        current.item, index.item = index.item, current.item

                    index = index.next
                current = current.next


class CircularLinkedList:
    """
        It is used in multiplayer games to give a chance to each player to play the game.
        Multiple running applications can be placed in a circular linked list on an operating system. The os keeps on
            iterating over these applications.
    """

    def __init__(self):
        self.last = None

    def add_to_empty(self, data):

        new_node = Node(data)
        self.last = new_node

        # create link to itself
        self.last.next = self.last

    def add_front(self, data):

        if self.last is None:
            return self.add_to_empty(data)

        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node

    def add_end(self, data):

        if self.last is None:
            return self.add_to_empty(data)

        new_node = Node(data)
        new_node.next = self.last.next

        self.last.next = new_node
        self.last = new_node

    def add_after(self, data, item):

        if self.last is None:
            return None

        new_node = Node(data)
        p = self.last.next
        while p:

            if p.data == item:
                new_node.next = p.next
                p.next = new_node

                if p == self.last:
                    self.last = new_node

            p = p.next
            if p == self.last.next:
                print(item, "The given node is not present in the list")
                break

    def delete_node(self, last, key):

        if last is None:
            return

        # If the list contains only a single node
        if last.data == key and last.next == last:
            last = None

        temp = last
        d = None

        # if last node is to be deleted
        if last.data == key:

            # find the node before the last node
            while temp.next != last:
                temp = temp.next

            # point temp node to the next of last i.e. first node
            temp.next = last.next
            last = temp.next

        # travel to the node to be deleted
        while temp.next != last and temp.next.data != key:
            temp = temp.next

        # if node to be deleted was found
        if temp.next.data == key:
            d = temp.next
            temp.next = d.next

        return last

    def traverse(self):
        if self.last is None:
            print("The list is empty")
            return

        new_node = self.last.next
        while new_node:
            print(new_node.data, end=" ")
            new_node = new_node.next
            if new_node == self.last.next:
                break


#==============================================================
# Max-Heap data structure in Python
# todo make a class
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(num)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))



# Tree traversal in Python
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)



# Binary Tree in Python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()


# Binary Search Tree operations in Python
# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)

# DFS Graphs
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}

dfs(graph, '0')


import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print("Following is Breadth First Traversal: ")
bfs(graph, 0)
