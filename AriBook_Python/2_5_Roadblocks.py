import heapq


INF = 10**18
N = 4
R = 4
# 隣接リスト
G = [[[1, 100]],
        [[0, 100], [2, 250], [3, 200]],
        [[1, 250], [3, 100]],
        [[1, 200], [2, 100]]]

dist = [INF for i in range(4)]
dist2 = [INF for i in range(4)]

que = []
heapq.heapify(que)

dist[0] = 0
heapq.heappush(que, [0, 0])

while len(que) > 0:
    p = heapq.heappop(que)
    v, d = p[1], p[0]
    if dist2[v] < d:
        continue
    for i in range(len(G[v])):
        e = G[v][i]
        d2 = d + e[1]
        if dist[e[0]] > d2:
            dist[e[0]], d2 = d2, dist[e[0]]
            heapq.heappush(que, [dist[e[0]], e[0]])
        if dist2[e[0]] > d2 and dist[e[0]] < d2:
            dist2[e[0]] = d2
            heapq.heappush(que, [dist2[e[0]], e[0]])

print(dist2[-1])
