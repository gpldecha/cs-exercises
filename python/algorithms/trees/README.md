# Chapter 4

## 4.1 Route Between Nodes
**Given a directed graph, design an algorithm to find out whether there is a route between two nodes.**
  - Should ask if it is acyclic.
  - If there are cycles should use BFS as it is guaranteed to find a solutions
  - If space is not an issue could stop visiting nodes already visited. This can
  either be done by adding a flag to the tree or it can be done with a hashmap.

## 4.2  Minimal Tree
 Given a sorted (increasing order) array with unique integer elements,
 write an algorithm to create a binary search tree with minimal height.
 - use a queue to do bfs insertion
 highlighting

```python
  i, j = queue.popleft()
  middle =  int((j - i)/2) + i
  tree.insert(a[middle])
  queue.append((i, middle-1))
  queue.append((middle+1, j ))
```
 - The cost of this is O( N log N )
 - The issue is that insert operation is log N. There is a more efficient way of
 doing it.
 - The approach in the book is to create a minimal bst in the recursion.

### 4.3 List of Depths
 Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists
  - Hash table with keys being levels and entry is a linked list of nodes at that level.

### 4.4 Check Balanced
Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of
the two subtrees of any node never differ by more than one.

function to find height of binary tree
```python
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def is_balanced(node):
  if node is None: return True
  height_diff = abs(height(node.left) - height(node.right))
  if height_diff <= 1:
    return is_balanced(node.left) and is_balanced(node.right)
  else:
    return False
```

- not optimal done in N log N

### 4.5 Validate BST

Implement a function to check if a binary tree is a binary search tree.
