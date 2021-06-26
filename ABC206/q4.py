import sys
from io import StringIO
import unittest


sys.setrecursionlimit(100000)


def dfs(v, flag, G):
    if not flag[v]:
        return
    flag[v] = False
    for nx in G[v]:
        dfs(nx, flag, G)


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    flag = [False for i in range(200005)]
    G = [[] for i in range(200005)]
    for a in A:
        # Aに含まれる整数の個数
        if not flag[a]:
            flag[a] = True
            ans += 1

    p = 0
    q = n - 1

    while p < q:
        # 連結成分に追加
        G[A[p]].append(A[q])
        G[A[q]].append(A[p])
        p += 1
        q -= 1

    for i in range(1, 200001):
        # 連結成分探索
        if flag[i]:
            ans -= 1
            dfs(i, flag, G)

    print(ans)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """8
1 5 3 2 5 2 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 2 3 4 1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
200000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
