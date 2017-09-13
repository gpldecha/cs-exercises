# Sorting
## simple sorts
* Selection sort

  time: O(N²)
  space: O(N)

* [Insertion sort](https://www.coursera.org/learn/algorithms-part1/lecture/1hYlN/insertion-sort) 

 time: O(1/4 N²)
 space: O(1/4 N^2)

* Shell sort

 time: O(N^(3/2))
 
## advanced sorts
 * [Merge sort](https://www.coursera.org/learn/algorithms-part1/lecture/ARWDq/mergesort)
 
  time  : O(N log N)
  
  space : O(N)
  
  stable : usually
  
  * [Quick sort](https://www.coursera.org/learn/algorithms-part1/lecture/vjvnC/quicksort)

Invented by Tony Hoare, implementations (Lomuto partition scheme, Hoare scheme). The choice of the pivot's position is very important. 

"In the very early versions of quicksort, the leftmost element of the partition would often be chosen as the pivot element. Unfortunately, this causes worst-case behavior on already sorted arrays, which is a rather common use-case...." [Wikipedia]

 time: average 
 
## priority queue/heap

Efficient for keeping track of the maximum element. Two operations, *pop max*, *insert*.

**Heap definitions** The binary heap is a data structure that can efficiently support the basic priority-queue operations. In a binary heap, the items are stored in an array such that each key is guaranteed to be larger than (or equal to) the keys at two other specific positions. In turn, each of those keys must be larger than two more keys, and so forth. This ordering is easy to see if we view the keys as being in a binary tree structure with edges from each key to the two keys known to be smaller.

**Definition** A binary tree is heap-ordered if the key in each node is larger than (or equal to) the keys in that nodes two children (if any).


For N items, the heap algorithm requires no more than 1 + lg N compares for insert and no more than 2 lg N for remove the 
maximum.

 
# Resources

* [Introduction to algorithms](https://www.coursera.org/learn/introduction-to-algorithms/home/info)
* [bigocheatsheet](http://bigocheatsheet.com/)
