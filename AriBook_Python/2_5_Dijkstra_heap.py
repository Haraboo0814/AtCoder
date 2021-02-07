import numpy as np
import heapq

INF = 10**8
V = 7   # 頂点数

# cost[u][v]:辺e = (u, v)のコスト
cost = np.asarray([[INF for i in range(V)] for j in range(V)])
d = np.asarray([INF for i in range(V)])     # 頂点sからの最短距離
used = np.asarray([False for i in range(V)])
G = [[[1, 2], [2, 5]],
        [[0, 2], [2, 4], [3, 6], [4, 10]],
        [[0, 5], [3, 2], [1, 4]],
        [[1, 6], [5, 1], [2, 2]],
        [[5, 3], [6, 5], [1, 10]],
        [[6, 9], [4, 3], [3, 1]],
        [[4, 5], [5, 9]]]


def dijkstra(s):
    que = [(0, 0)]
    heapq.heapify(que)
    d[s] = 0

    while len(que) > 0:
        print(que)
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for i in range(len(G[v])):
            e = G[v][i]
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))


dijkstra(0)
print(d)
