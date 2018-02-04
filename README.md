# cs-exercises
A set of cs data structures exercises.

# STL Containers
[STL containers](http://www.cplusplus.com/reference/stl/)

### Sequence containers

Constant time access O(1)

* array: satic contiguous array  

* vector: dynamic contiguous array 

Non-constant time access O(N)

* [std::deque](http://www.cplusplus.com/reference/deque/deque/): double-ended queue.

    Not guaranteed to store all its elements in contiguous storage locations: accessing elements in a deque by offsetting a   pointer to another element causes undefined behavior.
    
    *vector  is the type of sequence that should be used by default. ... deque is the data structure of choice when most insertions and deletions take place at the beginning or at the end of the sequence.* [ref](https://www.codeproject.com/Articles/5425/An-In-Depth-Study-of-the-STL-Deque-Container)


* [std::forward_list](http://en.cppreference.com/w/cpp/container/forward_list): singly-linked list

* [std::list](http://en.cppreference.com/w/cpp/container/list): doubly-linked list 


## Associative containers

### **ordered**

Associative containers implement sorted data structures that can be quickly searched (O(log n) complexity).

* [std::map](http://en.cppreference.com/w/cpp/container/map)  is a **sorted** associative container that contains key-value pairs with **unique keys** and are usually implemented as a [red black tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree): **search**, **insert**, **delete**: **O(log n)**

* [std::multipmap](http://en.cppreference.com/w/cpp/container/multimap): contains a **sorted** list of key-value pairs, 
where multiple elements can have equivalent keys.

### **unordered**

Unordered associative containers implement unsorted (hashed) data structures that can be quickly searched (O(1) amortized, O(n) worst-case complexity).

* [std::unordered_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/). Internally unordered_map is implemented using Hash Table.
