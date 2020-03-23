from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node:
            if data < node.data:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(data)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(data)
                    return

    def insert_recursive(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        self._insert_recursive(data, self.head)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left:
                self._insert_recursive(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._insert_recursive(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        if self.head.data == data:
            return self.head
        node = self.head
        while node:
            if node.data == data:
                return node
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return None

def traversal(node):
    if node is None: return
    traversal(node.right)
    print(node.data)
    traversal(node.left)

def bfs(queue, get_neighbours, func=None):
    while len(queue) != 0:
        node, level = queue.popleft()
        if func is not None:
            func(node, level)
        next_nodes = get_neighbours(node)
        for next_node in next_nodes:
            queue.append((next_node, level+1))

def dfs(stack, get_neighbours, func=None):
    while len(stack) != 0:
        node = stack.pop()
        if func is not None:
            func(node)
        next_nodes = get_neighbours(node)
        next_nodes.reverse()
        for next_node in next_nodes:
            stack.append(next_node)

def get_bst_neighbours(node):
    if node.left and node.right:
        return [node.left, node.right]
    elif node.left and not node.right:
        return [node.left]
    elif not node.left and not node.right:
        return []


def get_levels(bst):
    from collections import deque
    queue = deque()
    queue.append((bst.head, 0))
    levels = dict()
    def add_to_levels(node, level):
        if level in levels:
            levels[level].append(node.data)
        else:
            levels[level] = [node.data]
    bfs(queue, get_bst_neighbours, add_to_levels)
    print(levels)

def do_dfs(bst):
    stack = [bst.head]
    print(bst.head.left.data)
    print(bst.head.right.data)
    print(' ')
    def print_function(node):
        print(node.data)
    dfs(stack, get_bst_neighbours, print_function)

def insert(tree, i, j, a):
    if i > j: return
    middle = int((j - i)/2) + i
    tree.insert(a[middle])
    print(a[middle])
    insert(tree, i, middle - 1, a)
    insert(tree, middle + 1, j, a)

def non_recursive_insert(tree, i, j, a):
    queue = deque()
    queue.append((i, j))
    while len(queue) != 0:
        i, j = queue.popleft()
        if i > j:
            continue
        l = i - j
        if l % 2 == 0:
            middle = int((j - i)/2)  + i
        else:
            middle = int((j - i)/2) + 1 + i

        tree.insert(a[middle])
        queue.append((i, middle-1))
        queue.append((middle+1, j))

def test_1():
    bst = BinaryTree()
    bst.insert(6)
    bst.insert(4)
    bst.insert(8)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.insert(9)

    get_levels(binary_trees)

if __name__ == "__main__":
    bst = BinaryTree()
    a = [1, 2, 3, 4, 5, 6, 7]
    non_recursive_insert(bst, 0, len(a)-1, a)

    get_levels(bst)
