
def sort(a, aux, lo, hi):
    



def merge(a, aux, lo, mid, hi):
    for i in range(lo, hi+1):
        aux[i] = a[i]
    i = lo
    j = mid+1
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1



if __name__ == "__main__":

    a = [2, 10, 5, 3, 11, 9, 6, 2, 1]
    # a = [2, 10, 5, 3]

    aux = a[:]
    sort(a, aux, 0, len(a)-1)
    print(a)
