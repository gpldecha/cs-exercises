from collections import deque

class State:

    def __init__(self, position):
        self.position = position
        self.parent = None

    def is_equal(self, state):
        return state.position[0] == self.position[0] and \
           state.position[1] == self.position[1]

def get_next_states(state, num_rows, num_cols, add_state):
    r, c = state.position
    next_states = list()
    if c + 1 < num_cols:
        add_state(r, c + 1, next_states)
    if c - 1 >= 0:
        add_state(r, c - 1, next_states)
    if r + 1 < num_rows:
        add_state(r + 1, c, next_states)
    if r - 1 >= 0:
        add_state(r - 1, c, next_states)
    return next_states

def count_turns(state):
    turns = 1
    direction = None
    drev_direction = None
    prev_state = state
    prev_direction = None
    while state.parent:
        state = state.parent
        direction = (state.position[0] - prev_state.position[0], \
                     state.position[1] - prev_state.position[1])
        if prev_direction:
            if direction[0] != prev_direction[0] or direction[1] != prev_direction[1]:
                turns = turns + 1
        prev_state = state
        prev_direction = direction
    return turns

def minimumMoves(grid, startX, startY, goalX, goalY):
    current_state = State((startX, startY))
    goal_state = State((goalX, goalY))
    visited_states = dict()
    num_rows = len(grid)
    num_cols = len(grid[0])

    def is_visited(r, c):
        key = r*num_cols + c
        if key in visited_states:
            return True
        else:
            visited_states[key] = None
            return False

    def is_valid(r, c):
        return grid[r][c] != 'X'

    def add_states(r, c, next_states):
        if not is_visited(r, c) and is_valid(r, c):
            next_states.append(State( (r, c ) ))

    q = deque()
    q.append(current_state)

    while not current_state.is_equal(goal_state):
        current_state = q.popleft()
        next_states = get_next_states(current_state, num_rows, num_cols, add_states)
        for next_state in next_states:
            next_state.parent = current_state
            q.append(next_state)
    return current_state

import copy
if __name__ == "__main__":
    grid = []
    grid.append(['.', 'X', '.'])
    grid.append(['.', 'X', '.'])
    grid.append(['.', '.', '.'])
    startX, startY, goalX, goalY = 0, 0, 0, 2
    state = minimumMoves(grid, startX, startY, goalX, goalY)
    print('Finished')
    print(count_turns(state))
