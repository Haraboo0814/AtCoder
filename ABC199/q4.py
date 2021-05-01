import sys
from io import StringIO
import unittest


now = 0


def resolve():
    n, m = map(int, input().split())
    G = [[] for i in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    ans = 1
    used = [0] * n
    col = [-1] * n
    vs = []

    # 閉路の探索
    def dfs(v):
        if used[v]:
            return
        used[v] = 1
        vs.append(v)
        for vi in G[v]:
            dfs(vi)

    # 彩色
    def dfs2(i):
        if i == len(vs):
            global now
            now += 1
            return
        v = vs[i]
        for c in range(3):
            col[v] = c
            ok = True
            for u in G[v]:
                if col[u] == c:
                    ok = False

            if not ok:
                continue
            dfs2(i + 1)
        col[v] = -1

    for i in range(n):
        if used[i]:
            continue
        vs = []
        dfs(i)
        col[vs[0]] = 0
        global now
        now = 0
        dfs2(1)
        ans *= now * 3

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
        input = """3 3
1 2
2 3
3 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 6
1 2
2 3
3 4
2 4
1 3
1 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 0"""
        output = """3486784401"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
