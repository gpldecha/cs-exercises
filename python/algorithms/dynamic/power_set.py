import copy

def generate_power(s):
    sets = list()
    power(s, sets)
    return sets

def power(s, sets):
    if s == []: return
    if s not in sets:
        sets.append(s)
    else:
        return
    for i in range(len(s)):
        new_s = list(s)
        new_s.pop(i)
        power(new_s, sets)


def Pr(n):
    if n == 0:
        return []
    elif n == 1:
        return [[], [1]]
    elif n == 2:
        return [[], [1], [2], [1, 2]]
    else:
        prev_set = Pr(n-1)
        prev_set2 = copy.deepcopy(prev_set)
        for i in range(len(prev_set2)):
            prev_set2[i].append(n)
        prev_set.extend(prev_set2)
        return prev_set

if __name__ == "__main__":

    s = ['x', 'y', 'z']
    sets = generate_power(s)
    print('generated power set')
    for s in sets:
        print(s)

    sets = Pr(3)
    print(sets)
    # for s in sets:
    #     print(s)
