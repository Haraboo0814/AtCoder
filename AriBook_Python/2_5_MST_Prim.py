import numpy as np

INF = 10**8
V = 7   # 頂点数

# cost[u][v]:辺e = (u, v)のコスト
cost = np.asarray([[INF for i in range(V)] for j in range(V)])
edge = [[0, 1, 2], [0, 4, 10], [1, 2, 1], [1, 3, 3], [1, 5, 7],
        [3, 5, 1], [3, 6, 5], [4, 5, 5], [5, 6, 8]]
for e in edge:
    cost[e[0]][e[1]] = e[2]
    cost[e[1]][e[0]] = e[2]

mincost = [INF for i in range(V)]
used = [False for i in range(V)]


def prim():
    mincost[0] = 0
    res = 0

    while True:
        v = -1
        # Xに属さない頂点のうちXからの辺のコストが最小になる頂点を探す
        for u in range(V):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u

        if v == -1:
            break
        used[v] = True  # 頂点vをXに追加
        res += mincost[v]   # 辺のコストを追加

        for u in range(V):
            mincost[u] = min(mincost[u], cost[v][u])

    return res


ans = prim()
print(ans)
