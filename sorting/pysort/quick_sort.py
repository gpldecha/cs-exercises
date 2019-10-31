def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def sort(a, lo, hi):
    if hi <= lo: return
    j = partition(a, lo, hi)
    sort(a, lo, j-1)
    sort(a, j+1, hi)


def partition(a, lo, hi):
    pivot_idx = int(lo + (hi-lo)/2)
    pivot = a[pivot_idx]
    i = lo
    j = hi

    while True:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i >= j: break
        swap(a, i, j)
    return j


if __name__ == "__main__":
    # a = [6, 5, 4, 3, 2, 1]
    a = [4, 6, 10, 7, 2, 3, 5]
    len(a)
    #sort(a, 0, len(a)-1)
    #j = partition(a, 0, len(a)-1)
    #print(j)
    print(a)
