def make_number_to_window_size(a, hash_map):
    stack = []
    a.append(0)
    for i, value in enumerate(a):
        if not stack or stack[-1][1] < value:
            stack.append((i, value))
        else:
            j = i
            while stack and stack[-1][1] >=  value:
                j, pre_value = stack.pop()
                window_size = i - j
                if pre_value in hash_map:
                    if hash_map[pre_value] < window_size:
                        hash_map[pre_value] = window_size
                else:
                    hash_map[pre_value] = window_size
            stack.append((j, value))
    a.pop()

def inverse_hash_map(hash_map, new_hash_map):
    # exchange keys and value:
    for value, window_size in hash_map.items():
        if window_size in new_hash_map:
            new_hash_map[window_size] = max(new_hash_map[window_size], value)
        else:
            new_hash_map[window_size] = value

def make_max_number_per_window_size(a, hash_map):
    solutions = list()
    for window_size in range(len(a), 0, -1):
        if window_size in hash_map:
            solutions.append(hash_map[window_size])
        else:
            solutions.append(solutions[-1])
    return solutions

def final_part(arr, max_window):
    ans = [0]*(len(arr)-1)
    v_ant = min(max_window.values())
    for i in range(len(arr)-1, 0, -1):
        if i in max_window and max_window[i] > v_ant:
            ans[i-1] = max_window[i]
            v_ant = max_window[i]
        else:
           ans[i-1] = v_ant
    return ans

def riddle(a):
    hash_map = dict()
    new_hash_map = dict()
    make_number_to_window_size(a, hash_map)
    inverse_hash_map(hash_map, new_hash_map)
    return final_part(a, new_hash_map) #make_max_number_per_window_size(a, new_hash_map)


if __name__ == "__main__":
    a = [6, 3, 5, 1, 12]
    a = [2, 6, 1, 12]
    a = [1, 2, 3, 5, 1, 13, 3]
    a = [3, 5, 4, 7, 6, 2]
    a = [6, 5, 4, 3, 2, 1]

    a = [11, 2, 3, 14, 5, 2, 11, 12]

    print(riddle(a))
    #hash_map = dict()
    #make_number_to_window_size(a, hash_map)
    #print(hash_map)

    #a = [1, 2, 3, 4, 5]

    # solutions = riddle(a)
    # print(solutions)

    # solutions = riddle(a)
    # print(solutions)
