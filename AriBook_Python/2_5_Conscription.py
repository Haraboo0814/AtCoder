INF = 10**18
N = 5
M = 5
R = 8
X = [4, 1, 0, 0, 3, 1, 4, 2]
Y = [3, 3, 0, 1, 3, 3, 2, 2]
D = [6831, 4583, 6592, 3063, 4975, 2049, 2104, 781]

V = N + M
E = R

edge = []


def kruskal():
    edge.sort(key=lambda x: x[2])   # 辺のコストを小さい順にソート
    uf = UnionFind(V)
    res = 0

    for e in edge:
        if not uf.same(e[0], e[1]):
            uf.unite(e[0], e[1])
            res += e[2]

    return res


class UnionFind():

    def __init__(self, n):
        self.n = n
        # parents[x] = y: xの親がy
        # aが親なら -size(初期値-1)
        self.parents = [-1] * n

    # グループの根を探索
    def find(self, x):
        if self.parents[x] < 0:  # xが木の根の場合
            return x
        # 親へ再帰
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # グループの併合
    def unite(self, x, y):
        # x, yの根を探索
        x = self.find(x)
        y = self.find(y)
        if x == y:  # 同じ木に属する場合
            return
        # 計算速度のため、小さい方の根を大きい方の根につける
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]  # サイズを加算
        self.parents[y] = x  # 親の張り替え

    # 同じグループに属するか判定
    def same(self, x, y):
        # 根を比較し同じならtrue
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]  # 負で保存してあるため

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


# solve
for i in range(R):
    edge.append([X[i], N + Y[i], -D[i]])

print(10000 * (N + M) + kruskal())
