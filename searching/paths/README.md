# Algorithms related to path search

## Dijkstra

Implementation based on [wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). The caviate is 
that it needs a min-priority queue in which it is possible to decrease the priority (decrease-key). The standard 
heapq provided by python does not support it. I used the heapdict library in which we can change the priority of elements 
in the queue/heap.

  * cannot naturally handle negative weights
  * if a FIFO queue is used dijikstra's method degenerates to a breadth-first-search
  * [wikipedia pseudocode](https://en.wikipedia.org/wiki/A%2a_search_algorithm): nodes cannot be re-visited, the cost function is assumed to be monotonic ([can-astar-visit-nodes-more-than-once](https://stackoverflow.com/questions/21441662/can-astar-visit-nodes-more-than-once))
  
## Bellman-Ford


## Floyd-Warshall

* Shortest pathh between all nodes.
* Positive or negative edges.
* No cycles
* O(nodes^3)
* key idea : dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])
