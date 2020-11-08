class Edge:
    def __init__(self, n_from, n_to, cost):
        self.n_from = n_from
        self.n_to = n_to
        self.cost = cost


es = []
MAX_V = 100000
MAX_E = 100000
INF = 10**8

V, E = map(int, input().split())
for i in range(E):
    f, t, c = map(int, input().split())
    es.append(Edge(f, t, c))
    es.append(Edge(t, f, c))
d = [INF for i in range(V)]


def shortest_path(s):
    d[s] = 0
    while True:
        update = False
        for e in es:
            if d[e.n_from] != INF and d[e.n_to] > d[e.n_from] + e.cost:
                d[e.n_to] = d[e.n_from] + e.cost
                update = True

        if not update:
            break


shortest_path(0)
print(d)
