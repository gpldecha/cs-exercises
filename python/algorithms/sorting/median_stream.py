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


class MedianStream:

    def __init__(self, size):
        self.size = size
        self.window = list()
        self.is_even = self.size % 2 == 0
        self.median_idx = int(size/2)

    def get_median(self, number):
        if len(self.window) < self.size:
            self.window.append(number)
        else:
            print(self.window)
            element_to_remove = self.window[0]
            if self.is_even:
                median1 = quick_select(self.window, 0, len(self.window)-1, self.median_idx)
                median2 = quick_select(self.window, 0, len(self.window)-1, self.median_idx-1)
                median = (median1 + median2)/2.0
            else:
                median = quick_select(self.window, 0, len(self.window)-1, self.median_idx)

            for i in range(0, len(self.window)):
                if self.window[i] == element_to_remove:
                    self.window.pop(i)
                    break
            self.window.append(number)
            return median


if __name__ == "__main__":

    stream = MedianStream(3)
    for i in [10, 20, 30, 40, 50]:
        print(i)
        median = stream.get_median(i)
        if median is not None:
            print('median: {}'.format(median))
