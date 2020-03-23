def get_max_value_index(a):
    idx = 0
    v = a[0]
    for i in range(1, len(a)):
        if a[i] > v:
            v = a[i]
            idx = i
    return v, idx

def min_max(a):
    n = len(a)
    max_value, max_idx = get_max_value_index(a)
    solutions = [max_value]
    print(a)
    for i in range(n-1):
        if max_idx == 0:
            max_value = a[1]
            max_idx = 1
        else:
            if a[max_idx-1] < max_value:
                max_value = a[max_idx-1]
                max_idx = max_idx - 1
        for j in range(0, n - i - 1):
            a[j] = min(a[j], a[j+1])
            if a[j] >= max_value:
                max_value = a[j]
                max_idx = j
        solutions.append(max_value)
        print(a[:(n-i-1)])
    return solutions

import collections
def riddle_solution(arr):
    stack = [] #collections.deque()
    max_window = {}
    arr += [0,]
    for i, n in enumerate(arr):
        print('- {} -\n'.format(i))
        print(stack)
        if not stack or n > stack[-1][1]:
            stack.append((i, n))
        else:
            print('{} >= {} : {}'.format(stack[-1][1], n, stack[-1][1] >= n))
            while stack and stack[-1][1] >= n:
                print(' ')
                length_to_current = i-stack[-1][0]
                current_value = stack[-1][1]
                print('{} - {} = {}'.format(i, stack[-1][0], length_to_current))
                # print('{} < {}'.format(max_window[idx], stack[-1][1]))
                if length_to_current not in max_window or max_window[length_to_current] < current_value:
                    max_window[length_to_current] = current_value
                p = stack.pop()
            print(max_window)
            stack.append((p[0], n))
    return max_window
    ans = [0]*(len(arr)-1)
    v_ant = min(max_window.values())
    for i in range(len(arr)-1, 0, -1):
        if i in max_window and max_window[i] > v_ant:
            ans[i-1] = max_window[i]
            v_ant = max_window[i]
        else:
           ans[i-1] = v_ant
    return ans

from collections import defaultdict

def riddle(arr):
    stack = []
    arr.append(0)
    d=defaultdict(int)
    for i,j in enumerate(arr):           #making of step 2
        t=i
        while stack and stack[-1][0]>=j:
            val,li = stack.pop()
            d[j]=max(d[j],i-li+1)
            d[val]=max(d[val],i-li)
            t=li
        stack.append((j,t))
    return d

if __name__ == "__main__":
    a = [6, 3, 5, 1, 12]
    a = [2, 6, 1, 12]
    a = [1, 2, 3, 5, 1, 13, 3]
    a = [3, 5, 4, 7, 6, 2]
    a = [6, 5, 4, 3, 2, 1]

    a = [11, 2, 3, 14, 5, 2, 11, 12]
    #a = [1, 2, 3, 4, 5]

    # solutions = riddle(a)
    # print(solutions)

    solutions = riddle_solution(a)
    print(solutions)
