# cs-exercises
A set of cs data structures exercises.

# Data strcutures
[STL containers](http://www.cplusplus.com/reference/stl/)


## Associative containers

### **ordered**

Associative containers implement sorted data structures that can be quickly searched (O(log n) complexity).

* [std::map](http://en.cppreference.com/w/cpp/container/map)  is a **sorted** associative container that contains key-value pairs with **unique keys** and are usually implemented as a [red black tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree): **search**, **insert**, **delete**: **O(log n)**

* [std::multipmap](http://en.cppreference.com/w/cpp/container/multimap): contains a **sorted** list of key-value pairs, 
where multiple elements can have equivalent keys.

### **unordered**

Unordered associative containers implement unsorted (hashed) data structures that can be quickly searched (O(1) amortized, O(n) worst-case complexity).

* [std::unordered_map](http://www.cplusplus.com/reference/unordered_map/unordered_map/). Internally unordered_map is implemented using Hash Table.
