def count_steps(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return count_steps(n-1) + count_steps(n-2) + count_steps(n-3)


def count_steps_2(n):
    def move(i, j, arr):
        v = (i - j)
        if v < 0:
            return 0
        elif v == 0 or v == 1:
            return 1
        elif v == 2:
            return 2
        else:
            return arr[v]
    a = [0]*(n+1)
    a[0] = 1
    for i in range(1, n+1):
        a[i] = move(i, 1, a) + move(i, 2, a) + move(i, 3, a)
    return a

def countWays(n) :
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1) :
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    print(res)
    return res[n]

if __name__ == "__main__":

    steps = 8
    ans = count_steps(steps)
    print('num ways: {}'.format(ans))

    ans2 = count_steps_2(steps)
    print(ans2)

    ans3 = countWays(steps)
    print(ans3)
