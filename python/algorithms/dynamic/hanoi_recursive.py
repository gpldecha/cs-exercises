
def move_top(origin, destination):
    value = origin.pop()
    destination.append(value)

def move(n, origin, destination, buffer):
    if n <= 0: return
    print('move1({},{},{},{})'.format(n-1, origin[0], buffer[0], destination[0]))
    move(n-1, origin, buffer, destination)
    move_top(origin, destination)
    print('move {} -> {}'.format(origin[0], destination[0]))
    print('move2({},{},{},{})'.format(n-1, buffer[0], destination[0], origin[0]))
    move(n-1, buffer, destination, origin)


if __name__ == "__main__":
    towers = dict()
    towers['a'] = ['a', 3, 2, 1]
    towers['b'] = ['b']
    towers['c'] = ['c']

    move(3, towers['a'], towers['c'], towers['b'])

    print('finished')
    print(towers)
