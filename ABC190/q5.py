import sys
from io import StringIO
import unittest
from collections import deque
INF = 1 << 30


"""
https://atcoder.jp/contests/abc190/editorial/630
"""


def resolve():
    n, m = map(int, input().split())
    G = [list()for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)

    k = int(input())
    C = list(map(int, input().split()))
    for i in range(k):
        C[i] -= 1

    def BFS(s):
        cost = [INF] * n
        cost[s] = 0
        q = deque([s])
        while q:
            x = q.popleft()
            for y in G[x]:
                if cost[y] > cost[x] + 1:
                    cost[y] = cost[x] + 1
                    q.append(y)
        return [cost[c] for c in C]

    cost = [BFS(c) for c in C]

    dp = [[INF] * k for i in range(1 << k)]
    for i in range(k):
        dp[1 << i][i] = 1

    for bit in range(1 << k):
        for i in range(k):
            if dp[bit][i] == INF:
                continue
            for j in range(k):
                if bit & 1 << j:
                    continue
                if dp[bit ^ 1 << j][j] > dp[bit][i] + cost[i][j]:
                    dp[bit ^ 1 << j][j] = dp[bit][i] + cost[i][j]

    ans = min(dp[-1])
    if ans == INF:
        ans = -1
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
        input = """4 3
1 4
2 4
3 4
3
1 2 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 4
2 4
1 2
3
1 2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10
3 9
3 8
8 10
2 10
5 8
6 8
5 7
6 7
1 6
2 4
4
1 2 7 9"""
        output = """11"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
