from queue import Queue

from heapdict import heapdict

def astar_search(start, target, adjacency, heuristic):
    pass



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

