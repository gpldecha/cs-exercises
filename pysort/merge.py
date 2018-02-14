import copy

def sort(a):
    if len(a) < 2: return a
    b = list(a)
    split_and_merge(a, b, 0, len(a))
    return a


def split_and_merge(a, b, low, high):
    if low < high:
        middle = int((low+high)/2)

        split_and_merge(a, b, low, middle)
        split_and_merge(a, b, middle+1, high)
        merge(a, b, low, middle, high)


def merge(a, b, low, middle, high):
    for i in range(low, min(high+1, len(a))):
        b[i] = a[i]

    left = low
    right = middle+1
    curr = low

    while left <= middle and right < min(high+1, len(a)):
        if b[left] < b[right]:
            a[curr] = b[left]
            left += 1
        else:
            a[curr] = b[right]
            right += 1
        curr += 1

    remainder = middle-left
    for i in range(remainder+1):
        a[curr+i] = b[left+i]


if __name__ == "__main__" :

    print(sort([6, 5, 4, 3, 2, 1]))
    print(sort([6]))
    print(sort([6, 5]))
    print(sort([1, 2]))

