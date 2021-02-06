import numpy as np

INF = 10**8
V = 7   # 頂点数

# cost[u][v]:辺e = (u, v)のコスト
cost = np.asarray([[INF for i in range(V)] for j in range(V)])
d = np.asarray([INF for i in range(V)])     # 頂点sからの最短距離
used = np.asarray([False for i in range(V)])
edge = [[0, 1, 2], [0, 2, 5], [1, 2, 4], [1, 3, 6], [1, 4, 10], [2, 3, 2],
        [3, 5, 1], [4, 5, 3], [4, 6, 5], [5, 6, 9], [1, 0, 2], [2, 0, 5],
        [2, 1, 4], [3, 1, 6], [4, 1, 10], [3, 2, 2], [5, 3, 1], [5, 4, 3],
        [6, 4, 5], [6, 5, 9]]
for e in edge:
    cost[e[0]][e[1]] = e[2]


def dijkstra(s):
    d[s] = 0
    while True:
        v = -1
        for u in range(V):
            # 使われていない頂点のうち距離が最小のものを探索
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break
        used[v] = True
        for u in range(V):
            d[u] = min(d[u], d[v] + cost[v][u])


dijkstra(0)
print(d[-1])
