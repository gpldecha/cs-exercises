

def sort(a):

    if len(a) < 2: return a

    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


if __name__ == "__main__" :

    print(sort([6, 5, 4, 3, 2, 1]))
    print(sort([6]))
    print(sort([6, 5]))
    print(sort([1, 2]))
