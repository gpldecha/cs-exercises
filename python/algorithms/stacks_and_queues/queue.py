class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            # move the tail forward
            self.tail = self.tail.next

    def remove(self):
        if self.head is None: return None
        data = self.head.data
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        return data


if __name__ == "__main__":
        queue = Queue()
        for i in range(5):
            queue.add(i)
        for i in range(5):
            print(queue.remove())
