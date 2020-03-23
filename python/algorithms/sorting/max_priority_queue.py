class Item:

    def __init__(self, key, value):
        self.value = value
        self.key = key


class MaxPriorityQueue:

    def __init__(self):
        self.pq = [Item(None, None)]
        self.index = dict()

    def insert(self, key, value):
        self.pq.append(Item(key, value))
        pq_index = len(self.pq)-1
        self.index[key] = pq_index
        self._swim(pq_index)

    def remove_root(self):
        self._swap(self.pq, 1, len(self.pq)-1)
        item = self.pq.pop()
        del self.index[item.key]
        self._sink(1)
        return item

    def change_priority(self, key, value):
        i = self.index[key]
        if value < self.pq[i].value:  # priority as decreased
            self.pq[i].value = value
            self._sink(i)
        else: # priority has increased
            self.pq[i].value = value
            self._swim(i)

    def _swim(self, current):
        if current == 1:
            return
        parent = int(current/2)
        if self.pq[current].value > self.pq[parent].value:
            self._swap(self.pq, current, parent)
            return self._swim(parent)
        else:
            return

    def _sink(self, current):
        if current >= len(self.pq)-1:
            return
        left_child = current*2
        right_child = current*2 + 1

        if left_child >= len(self.pq) and right_child > len(self.pq): return

        # only consider left side
        if right_child >= len(self.pq):
            if self.pq[current].value < self.pq[left_child].value:
                self._swap(self.pq, current, left_child)
                return self._sink(left_child)
            else:
                return

        if self.pq[current].value < self.pq[left_child].value and self.pq[current].value < self.pq[right_child].value:
            if self.pq[left_child].value > self.pq[right_child].value:
                self._swap(self.pq, current, left_child)
                return self._sink(left_child)
            else:
                self._swap(self.pq, current, right_child)
                return self._sink(right_child)
        elif self.pq[current].value < self.pq[left_child].value:
            self._swap(self.pq, current, left_child)
            return self._sink(left_child)
        elif self.pq[current].value < self.pq[right_child].value:
            self._swap(self.pq, current, right_child)
            return self._sink(right_child)
        else:
            return

    def _swap(self, a, i, j):
        self.index[self.pq[i].key] = j
        self.index[self.pq[j].key] = i
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    def __len__(self):
        return len(self.pq)

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n < len(self):
            item = self.pq[self.n]
            self.n += 1
            return item.key, item.value
        else:
            raise StopIteration

if __name__ == "__main__":
    queue = MaxPriorityQueue()

    items = [(0, 3), (1, 4), (2, 5)]

    for (key, value) in items:
        queue.insert(key, value)

    queue.change_priority(0, 10)
    queue.change_priority(1, 6)

    for (key, value) in queue:
        print('{} {}'.format(key, value))

    max_value = queue.remove_root()
    print(max_value.value)

    print(' ')
    for (key, value) in queue:
        print('{} {}'.format(key, value))

    # max_value = queue.remove_root()
    # print(max_value.value)
