class Item:

    def __init__(self, value, item):
        self.key = value
        self.item = item


class MaxPriorityQueue:

    def __init__(self):
        self.pq = [Item(None, None)]
        self.index = dict()

    def insert(self, k, item):
        self.pq.append(Item(k, item))
        item_index = len(self.pq)-1
        self.index[k] = item_index
        self._swim(item_index)

    def remove_root(self):
        self._swap(self.pq, 1, len(self.pq)-1)
        item = self.pq.pop()
        del self.index[item.key]
        self._sink(1)

    def change(self, k, item):
        i = self.index[k]
        if k < self.pq[i].key:

        else:
            self.pq[i].key = k
            self.pq[i].item = item


    def _swim(self, current):
        if current == 1:
            return
        parent = int(current/2)
        if self.pq[current].key > self.pq[parent].key:
            self._swap(self.pq, current, parent)
            return self._swim(parent)
        else:
            return

    def _sink(self, current):
        if current >= len(self.pq)-1:
            return
        left_child = current*2
        right_child = current*2 + 1
        if self.pq[current].key < self.pq[left_child].key and self.pq[current].key < self.pq[right_child].key:
            if self.pq[left_child].key > self.pq[right_child].key:
                self._swap(self.pq, current, left_child)
                return self._sink(left_child)
            else:
                self._swap(self.pq, current, right_child)
                return self._sink(right_child)
        elif self.pq[current].key < self.pq[left_child].key:
            self._swap(self.pq, current, left_child)
            return self._sink(left_child)
        elif self.pq[current].key < self.pq[right_child].key:
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


if __name__ == "__main__":