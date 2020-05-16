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


n = 100
k = 7
query = [(1, 101, 1), (2, 1, 2), (2, 2, 3),
         (2, 3, 3), (1, 1, 3), (2, 3, 1), (1, 5, 5)]

uf = UnionFind(n * 3)
ans = 0
for q in query:
    t, x, y = q[0], q[1] - 1, q[2] - 1
    if x < 0 or n <= x or y < 0 or n <= y:
        print(q)
        ans += 1
        continue

    if t == 1:
        # x = y, 同種のuf
        if uf.same(x, y + n) or uf.same(x, y + 2 * n):
            print(q)
            ans += 1
        else:
            uf.unite(x, y)
            uf.unite(x + n, y + n)
            uf.unite(x + 2 * n, y + 2 * n)

    else:
        # x != y, 食べるuf
        if uf.same(x, y) or uf.same(x, y + 2 * n):
            print(q)
            ans += 1
        else:
            uf.unite(x, y + n)
            uf.unite(x + n, y + 2 * n)
            uf.unite(x + 2 * n, y)

print(ans)
