class Node:

    def __init__(self, value, node):
        self.value = value
        self.next = node

class SingleLinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        current = self.head
        while current.next != None:
            current = current.next
            if current is None:
                return
        current.next = Node(value, None)

    def pop_front(self):
        if self.head is None: return
        value = self.head.value
        self.head = self.head.next
        return value

    def push_front(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        next_head = self.head
        self.head = Node(value, next_head)

    def remove(self, value):
        if self.head is None: return
        if value == self.head.value:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current.value != value:
            previous = current
            current = current.next
            if current is None:
                return
        previous.next = current.next

    def print_values(self):
        if self.head is None: print('No values!')
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current is None: return

def test_case_base():
        print('test_case_base')
        single_linked_list = SingleLinkedList()
        single_linked_list.append(1)
        single_linked_list.append(2)
        single_linked_list.append(3)
        single_linked_list.print_values()
        print('remove 2')
        single_linked_list.remove(2)
        single_linked_list.print_values()

        print('remove 3')
        single_linked_list.remove(3)
        single_linked_list.print_values()

        print('remove 1')
        single_linked_list.remove(1)
        single_linked_list.print_values()

def test_pop_front():
    print('test_case_base')
    single_linked_list = SingleLinkedList()
    single_linked_list.append(1)
    single_linked_list.append(2)
    single_linked_list.append(3)
    print('pop front')
    print(single_linked_list.pop_front())
    print(single_linked_list.pop_front())
    print(single_linked_list.pop_front())
    print(single_linked_list.pop_front())

def test_pop_front_with_objects():
    print('pop front with objects')
    single_linked_list = SingleLinkedList()
    single_linked_list.append([1])
    single_linked_list.append([2])
    single_linked_list.append([3])
    print('pop front')
    print(single_linked_list.pop_front())
    print(single_linked_list.pop_front())
    print(single_linked_list.pop_front())
    print(single_linked_list.pop_front())

def test_push_front():
    print('test push front')
    single_linked_list = SingleLinkedList()
    single_linked_list.push_front(1)
    single_linked_list.push_front(2)
    single_linked_list.push_front(3)
    single_linked_list.print_values()

if __name__ == "__main__":
    test_push_front()
