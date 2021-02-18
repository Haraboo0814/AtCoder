import numpy as np

INF = 10**8
V = 7   # 頂点数

# d[u][v]:辺e = (u, v)のコスト
d = np.asarray([[INF for i in range(V)] for j in range(V)])
edge = [[0, 1, 2], [0, 2, 5], [1, 2, 4], [1, 3, 6], [1, 4, 10], [2, 3, 2],
        [3, 5, 1], [4, 5, 3], [4, 6, 5], [5, 6, 9], [1, 0, 2], [2, 0, 5],
        [2, 1, 4], [3, 1, 6], [4, 1, 10], [3, 2, 2], [5, 3, 1], [5, 4, 3],
        [6, 4, 5], [6, 5, 9]]
for e in edge:
    d[e[0]][e[1]] = e[2]


def warshall_floyd():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


warshall_floyd()
print(d)
