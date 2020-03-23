import math

class MinHeap:

    def __init__(self):
        self.h = list()

    def insert(self, data):
        self.h.append(data)
        i = len(self.h)-1
        j = self._get_parent(i)
        # bubble up
        while self.h[j] > self.h[i]:
            self.h[i], self.h[j] = self.h[j], self.h[i]
            i = j
            j = self._get_parent(i)

    def pop(self):
        self.swap(0, len(self.h)-1)
        min_value = self.h.pop()
        #print('start')
        #print(self.h)
        # bubble down
        i = 0
        left = self._get_left_child(i)
        right = self._get_right_child(i)
        is_left_valid = self._is_valid(left)
        is_right_valid = self._is_valid(right)

        #print('i: {} left: {} right: {}'.format(i, left, right))

        is_finished = False
        while not is_finished:
            #print('i: {} left: {} is valid {} right: {} is valid {}  len: {}'.format(
            #i, left, is_left_valid, right, is_right_valid, len(self.h)))

            if is_left_valid and self.h[left] < self.h[i]:
                self.swap(left, i)
                i = left
            elif is_right_valid and self.h[right] < self.h[i]:
                self.swap(right, i)
                i = right

            left = self._get_left_child(i)
            right = self._get_right_child(i)
            is_left_valid = self._is_valid(left)
            is_right_valid = self._is_valid(right)

            if not is_left_valid and not is_right_valid:
                is_finished = True
            elif is_left_valid and is_right_valid and left.h[left] >= self.h[i] and left.h[right] >= self.h[i]:
                is_finished = True
            elif is_left_valid and not is_right_valid and self.h[left] >= self.h[i]:
                is_finished = True
            elif  not is_left_valid and is_right_valid and self.h[right] >= self.h[i]:
                is_finished = True
        return min_value
        #print('final heap: {}'.format(self.h))


    def swap(self, i, j):
        self.h[i], self.h[j] = self.h[j], self.h[i]

    def _is_valid(self, i):
        return i <= len(self.h) - 1

    def _get_parent(self, i):
        return int((i-1)/2)

    def _get_left_child(self, i):
        return i*2 + 1

    def _get_right_child(self, i):
        return i*2 + 2



if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(10)
    heap.insert(8)
    heap.insert(2)
    heap.insert(12)
    heap.insert(7)

    print(heap.h)
    print('pop: {}'.format(heap.pop()))
    print('pop: {}'.format(heap.pop()))
    print('pop: {}'.format(heap.pop()))
    print('pop: {}'.format(heap.pop()))
    print('pop: {}'.format(heap.pop()))
