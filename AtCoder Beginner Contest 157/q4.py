class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]


N, M, K = map(int, input().split())
uf = UnionFind(N)
friends = [[] for _ in range(N)]    # 友達関係
blocks = [[] for _ in range(N)]     # ブロック関係

for i in range(M):
    a, b = map(int, input().split())
    # 相互友達関係の追加
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)
    # 併合
    uf.unite(a - 1, b - 1)

for i in range(K):
    c, d = map(int, input().split())
    if uf.same(c - 1, d - 1):
        # 同じグループ内の場合相互ブロック関係の追加
        blocks[c - 1].append(d - 1)
        blocks[d - 1].append(c - 1)

ans = []
for i in range(N):
    # グループ内の人数 - 自身 - ブロック人数 - 友達人数
    ans.append(uf.size(i) - 1 - len(blocks[i]) - len(friends[i]))
print(*ans)
