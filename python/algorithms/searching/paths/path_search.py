from queue import Queue
import numpy as np
from heapdict import heapdict

def astar_search(start, target, adjacency, heuristic):
    pass


def floyd_warshall(adjacency):
    num_states = len(adjacency)
    dist = np.ones(shape=(num_states, num_states))*np.inf
    next_ = np.zeros(shape=(num_states, num_states), dtype=np.int)
    for state in range(len(adjacency)):
        for next_state in adjacency[state, :]:
            if next_state != -1:
                dist[state, next_state] = 1
                next_[state, next_state] = next_state

    for k in range(num_states):
        for j in range(num_states):
            for i in range(num_states):
                if dist[i, j] > dist[i, k] + dist[k, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    next_[i, j] = next_[i, k]
    return dist, next_


def get_path(next_, u, v):
    if next_[u, v] == np.inf:
        return []
    path = [u]
    while u != v:
        u = next_[u, v]
        path.append(u)
    return path


def djikstra_search(start, target, adjacency):
    queue = heapdict()
    cost_so_far = dict()
    cost_so_far[start] = 0.0

    previous = dict()

    queue[start] = cost_so_far[start]

    while len(queue) != 0:
        state, state_cost = queue.popitem()

        if state == target:
            break

        for next_state in adjacency[state, :]:
            if next_state != -1:
                new_cost = state_cost + 1.0
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    queue[next_state] = new_cost
                    cost_so_far[next_state] = new_cost
                    previous[next_state] = state

    path = [target]
    while path[-1] != start:
        path.append(previous[path[-1]])
    return path


def breadth_first_search(start, target, adjacency):
    open_set = Queue()
    open_set.put(start)
    closet_set = set()
    previous = dict()

    while not open_set.empty():
        state = open_set.get()
        closet_set.add(state)

        if state == target:
            break

        for next_state in adjacency[state, :]:
            if next_state != -1 and next_state and next_state not in closet_set:
                open_set.put(next_state)
                previous[next_state] = state

    path = [target]
    while path[-1] != start:
        path.append(previous[path[-1]])
    return path

