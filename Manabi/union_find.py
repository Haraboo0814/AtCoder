class UnionFind():
    '''
    グループ分けを木構造で管理するデータ構造
    以下の二点を高速で行うことができるのがメリット．
    ・要素xと要素yが同じグループに属するかどうかを判定したい
        → 要素xの根と要素yの根が同じならば同じグループ，
          要素xの根と要素yの根が同じでないならば異なるグループ
          にあることが分かる．
    ・要素xと要素yが別のグループに属する場合，
        要素xの属するグループと要素yの属するグループを併合する．
    '''

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
