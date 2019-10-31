
class Sort:

    def __init__(self):
        pass

    def sort(self, arr):
        self._sort(arr, 0, len(arr))

    def _sort(self, a, lo, hi):
        if hi <= lo: return
        j = self._partition(a, lo, hi)
        self._sort(a, lo, j-1)
        self._sort(a, j+1, hi)

    def _partition(self, a, lo, hi):
        pass



if __name__ == "__main__":
    print(sort([6, 5, 4, 3, 2, 1]))
