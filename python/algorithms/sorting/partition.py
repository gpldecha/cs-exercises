import copy


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def partition_lomuto(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i = i + 1
    swap(arr, i, hi)
    return i


def partition_hoare(a, lo, hi, pivot_idx):
    #   a[lo...pivot_idx-1] [pivot_idx] [pivot_idx+1...hi]
    pivot = a[pivot_idx]
    i = lo
    j = hi

    while True:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i >= j: break
        print('swap({},{})'.format(i, j))
        swap(a, i, j)
    return j


if __name__ == "__main__":
    # a = [4, 6, 10, 7, 2, 3, 5]
    # a = [1, 2, 3, 4, 5, 6, 7]
    #a = [7, 6, 5, 4, 3, 2, 1]
    a = [0, 1, 2, 3, 4, 5, 6]
    j = partition_hoare(a, 0, len(a) - 1, 0)
    print(a)
    print(j)
