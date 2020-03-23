def maxSubsetSum(array):
    max_tmp2 = array[0]
    max_tmp1 = max(array[0], array[1])
    best_maximum = max_tmp1
    for a in array[2:]:
        #print('{}  {}  {}'.format(a, max_tmp2, max_tmp1))
        current_maximum = max(max(max_tmp2+a, 0), best_maximum)
        best_maximum = max(best_maximum, current_maximum)
        max_tmp2 = max_tmp1
        max_tmp1 = current_maximum

    return best_maximum


if __name__  == "__main__":

    arr = [3, 7, 4, 6, 5]
    ans = maxSubsetSum(arr)
    print(ans)
