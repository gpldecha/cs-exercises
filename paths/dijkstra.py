import matplotlib.pyplot as plt
import numpy as np
from heapdict import heapdict

from utils import create_grid_adj, to_ij, to_idx


def find_path(a, adj_matrix):
    """
    :param a:   int, target node.
    :param adj_matrix: N x 4, grid world adjacency matrix.
    :return: list(int), list of gird indexes.
    """
    prev = -np.ones(len(adj_matrix), dtype=int)
    distances = np.ones(len(adj_matrix)) * np.inf
    distances[a] = 0.0
    hd = heapdict()
    for node in range(len(adj_matrix)):
        hd[node] = distances[node]
    hd[a] = distances[a]

    while len(hd) != 0:
        node, d = hd.popitem()
        for v in adj_matrix[node, :]:
            if v != -1:
                alt = distances[node] + 1
                if alt < distances[v]:
                    distances[v] = alt
                    prev[v] = node
                    hd[v] = distances[v]
    return distances, prev

if __name__ == "__main__":

    n = 200
    adj_matrix = create_grid_adj(n)

    distance, previous = find_path(to_idx(int(n/2), int(n/2), n), adj_matrix)

    plt.close('all')
    fig = plt.figure()
    grid_points = np.empty(shape=(n*n, 2))
    cax = plt.imshow(distance.reshape((n, n)), origin='lower')
    cbar = fig.colorbar(cax)
    max_show = 10.0
    plt.xticks(np.arange(0, n+1, max(1, int(float(n)/max_show))))
    plt.yticks(np.arange(0, n+1, max(1, int(float(n)/max_show))))
    plt.axis('equal')
    plt.show()


