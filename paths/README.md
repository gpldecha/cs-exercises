# Algorithms related to path search

## Dijkstra

Implementation based on [wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). The caviate is 
that it needs a min-priority queue in which it is possible to decrease the priority (decrease-key). The standard 
heapq provided by python does not support it. I used the heapdict library in which we can change the priority of elements 
in the queue/heap.

  * cannot naturally handle negative weights
  * if a FIFO queue is used dijikstra's method degenerates to a breadth-first-search
