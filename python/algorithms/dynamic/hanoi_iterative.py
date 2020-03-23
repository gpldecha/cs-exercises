def is_empty(a, h):
    return len(h[a]) == 0

def is_even(a, h):
    return h[a][-1] % 2 == 0

def is_odd(a, h):
    return h[a][-1] % 2 != 0

def is_legal(start, end, h):
    if is_empty(end, h): return True
    if h[end][-1] > h[start][-1]: return True
    return False

def get_next_move(h, last_start, last_end):
    ends = ['a', 'b', 'c']
    starts = [s for s in ['a', 'b', 'c'] if s != last_end]
    solutions = list()
    for s in starts:
        if is_empty(s, h): # cannot move a piece twice
            continue
        for e in ends:
            if is_empty(e, h):
                solutions.append((s, e))
                continue
            if is_even(s, h) and is_even(e, h):
                continue
            if is_odd(s, h) and is_odd(e, h):
                continue
            if not is_legal(s, e , h):
                continue

            solutions.append((s, e))

    if len(solutions) == 1:
        return solutions[0]
    else:
        for (s, e) in solutions:
            if not is_empty(e, h):
                return s, e



if __name__ == "__main__":
    h = dict()
    h['a'] = [5, 4, 3, 2, 1]
    h['b'] = []
    h['c'] = []

    optimal_moves = 2**(len(h['a'])) - 1
    moves = 1

    def is_finished(h):
        return h['c'] == [5, 4, 3, 2, 1]

    def move(start, end):
        value = h[start].pop()
        h[end].append(value)

    start = 'a'
    if len(h['a']) % 2 == 0: # even
        end = 'b'
    else:
        end = 'c'

    move(start, end)
    while not is_finished(h):
        moves += 1
        print(' ')
        print(h)
        start, end = get_next_move(h, start, end)
        move(start, end)
    print(' ')
    print(h)
    print('moves: {}'.format(moves))
    print('optimal moves: {}'.format(optimal_moves))
