

def sort(a):

    has_swapped = True
    n = len(a)
    if n < 2: return a

    while has_swapped or n == 0:
        has_swapped = False
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                has_swapped = True
        n -= 1
    return a


if __name__ == "__main__" :

    print(sort([6, 5, 4, 3, 2, 1]))
    print(sort([6]))
    print(sort([6, 5]))
    print(sort([1, 2]))
