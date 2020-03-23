from path_search import breadth_first_search
from path_search import djikstra_search
from path_search import floyd_warshall, get_path
from utils import create_grid_adj, to_ij, to_idx
import matplotlib.pyplot as plt
import numpy as np


def plot_path(path, start_idx, end_idx, n):
    plt.close('all')
    fig = plt.figure()
    plt.title('breadth first search')
    grid_points = np.empty(shape=(n*n, 2))
    for i in range(n*n):
        grid_points[i, :] = to_ij(i, n)
    plt.scatter(grid_points[:, 0], grid_points[:, 1])

    start = to_ij(start_idx, n)
    plt.scatter(start[0], start[1], marker='o', edgecolors='g', linewidths=5)

    end = to_ij(end_idx, n)
    plt.scatter(end[0], end[1], marker='o', edgecolors='r', linewidths=5)

    for i in range(len(path)-1):
        a = to_ij(path[i], n)
        b = to_ij(path[i+1], n)
        line = np.array([a, b])
        plt.plot(line[:, 0], line[:, 1], '-k')

    max_show = 10.0
    plt.xticks(np.arange(0, n+1, max(1, int(float(n)/max_show))))
    plt.yticks(np.arange(0, n+1, max(1, int(float(n)/max_show))))
    plt.axis('equal')
    plt.show()

def example_path_search():
    n = 10
    adj_matrix = create_grid_adj(n)

    start_idx = to_idx(0, 0, n)
    end_idx = to_idx(8, 8, n)

    # path = breadth_first_search(start=start_idx, target=end_idx, adjacency=adj_matrix)
    path = djikstra_search(start=start_idx, target=end_idx, adjacency=adj_matrix)
    plot_path(path, start_idx, end_idx, n)



def example_floyd_walsh():
    n = 10
    adj_matrix = create_grid_adj(n)

    dist, next_ = floyd_warshall(adj_matrix)

    start_idx = to_idx(0, 0, n)
    end_idx = to_idx(8, 8, n)
    path = get_path(next_, start_idx, end_idx)

    plot_path(path, start_idx, end_idx, n)


    print('path     {}'.format(path))
    print('next_    {}'.format(next_))

if __name__ == "__main__":
    example_floyd_walsh()



