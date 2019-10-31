import random


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


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


def lomuto(arr, lo, hi):
    pivot_index = int(lo + (hi-lo)/2)
    pivot = arr[pivot_index]
    swap(arr, pivot_index, hi)
    i = lo
    print(arr)
    print('start')
    for j in range(lo, hi):
        if arr[j] <= pivot:
            print('swap({},{})'.format(i, j))
            swap(arr, i, j)
            i = i + 1
        print(arr)
    print('last swap({},{})'.format(i, hi))
    swap(arr, i, hi)
    print(arr)
    return i


def quick_select(arr, lo, hi, k):
    if lo == hi:
        return arr[lo]

    pivot_index = partition(arr, lo, hi)

    if pivot_index == k:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, lo, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, hi, k)


if __name__ == "__main__":
    # median is 5
    a = [4, 6, 10, 7, 2, 3, 5]
    print(len(a)/2)
    # a = [1, 2, 3, 4, 5, 6, 7]
    #v = quick_select(a, 0, len(a)-1, 3)
    #print(' ')
    #print(v)
