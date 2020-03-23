def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = -1  # or: float('-inf')
    current_sum = 0
    trac = []
    print(' x   c   b')
    for l, x in enumerate(numbers):

        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)

        print('{0:2d}  {1:2}  {2:2}'.format(x, current_sum, best_sum))
    return best_sum
# when the sum of elements up to the ith position
# is smaller than zero, we reset the sum.
# This means that a possible future subset may
# not include elements prior to the ith position.

if __name__ == "__main__":

    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-1, -1, -1, -52, -30]
    best_sum = max_subarray(arr)
    print(best_sum)
