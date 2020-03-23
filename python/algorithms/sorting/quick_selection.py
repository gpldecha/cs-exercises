import math
import random

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def lomuto(arr, lo, hi, pivot_index):
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


def select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_index = left + math.floor(random.random() % (right - left + 1))
    pivot_index = lomuto(arr, left, right, pivot_index)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, left, pivot_index - 1, k)
    else:
        return select(arr, pivot_index + 1, right, k)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]

    v = select(a, 0, len(a)-1, 1)
    print(v)

