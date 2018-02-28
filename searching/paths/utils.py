import numpy as np


def to_idx(i, j, n):
    if i >= n or i < 0: return -1
    if j >= n or j < 0: return -1
    if i*n + j >= n*n: return -1
    return i*n + j


def to_ij(idx, n):
    j = idx % n
    i = int((idx - j)/n)
    return i, j


def create_grid_adj(size):
    A = np.zeros(shape=(size*size, 4), dtype=int)
    for idx in range(0, size*size):
        i, j = to_ij(idx, size)
        A[idx, 0] = to_idx(i=i, j=(j + 1), n=size)
        A[idx, 1] = to_idx(i=i, j=(j - 1), n=size)
        A[idx, 2] = to_idx(i=(i + 1), j=j, n=size)
        A[idx, 3] = to_idx(i=(i - 1), j=j, n=size)
    return A


if __name__ == "__main__":
   A = create_grid_adj(3)
   print(A)