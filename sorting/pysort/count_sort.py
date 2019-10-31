import collections
# https://rosettacode.org/wiki/Sorting_algorithms/Counting_sort


def count_sort(arr, min, max):
    count = [0]*(max - min + 1)
    for number in arr:
        count[number - min] = count[number - min] + 1
    z = 0
    for i in range(min, max+1):
        while count[i - min] > 0:
             arr[z] = i
             z += 1
             count[i - min] = count[i - min] - 1


def count_sort_median(arr, min, max, is_even):
    count = [0] * (max - min + 1)
    for number in arr:
        count[number - min] = count[number - min] + 1

    idx = len(arr) / 2

    # z = 0
    # for i in range(min, max + 1):
    #     for j in range(count[i - min]):
    #         z += 1
    #         if z >= idx:
    #             return i


def get_median(counts, idx):
    z = 0
    expense_two = 0
    for i in range(201):
        for j in range(counts[i]):
            if z >= idx:
                return i, (i + expense_two)*0.5
            expense_two = i
            z += 1


class MedianFilter:

    def __init__(self, d):
        self.window_size = d
        self.counts = [0]*201
        self.t = 0
        self.idx = int(d/2)
        self.is_even = d % 2 == 0
        self.buffer = [0]*(d+1)
        self.buffer_idx = 0
        self.notifications = 0

    def update(self, expenditure):
        self.buffer[self.buffer_idx] = expenditure
        self.buffer_idx = (self.buffer_idx + 1)%(self.window_size+1)

        if self.t < self.window_size:
            self.counts[expenditure] += 1
            self.t += 1
            return
        median_odd, median_even = get_median(self.counts, self.idx)
        if self.is_even:
            median = median_even
        else:
            median = median_odd
        if expenditure >= 2.0*median:
            self.notifications += 1

        expenditure_remove = self.buffer[self.buffer_idx]
        self.counts[expenditure] += 1
        self.counts[expenditure_remove] -= 1


def activityNotifications(expenditure, d):
    pass

    

if __name__ == "__main__":
    expenses = [10, 20, 30, 40, 80]
    d = 4
    filter = MedianFilter(d)
    for i, expense in enumerate(expenses):
        print(i)
        filter.update(expense)

    print(filter.notifications)

    # a = [3, 4, 5, 3, 3, 4, 10, 9]
    # median = count_sort_median(a, 3, 10, True)
    # print(median)
    #
    # idx_1 = int(len(a)/2)
    # a.sort()
    # print(a)
    # print(a[idx_1])
