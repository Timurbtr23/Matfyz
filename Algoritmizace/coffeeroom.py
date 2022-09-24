class Client:

    def __init__(self, name, priority):
        self.name = name
        self.priora = float(priority)


class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    def count(self):
        return len(self.queue)

    def add(self, element, priority):
        client = Client(element, priority)
        self.queue.append(client)

    def remove_largest(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i].priora > self.queue[max].priora:
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item


if __name__ == "__main__":
    pq = PriorityQueue()
    length = int(input())
    try:
        k = 0
        while pq.count() <= length:
            client = input().split()
            pq.add(client[0], client[1])
            if pq.count() == length:
                k = 1
                kek = pq.remove_largest()
                print(kek.name, kek.priora)
            elif k == 1:
                kek = pq.remove_largest()
                print(kek.name, kek.priora)
    except EOFError:
        while pq.count() != 0:
            kek = pq.remove_largest()
            print(kek.name, kek.priora)

