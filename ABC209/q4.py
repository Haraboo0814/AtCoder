import sys
from io import StringIO
import unittest
from collections import deque


def resolve():
    N, Q = map(int, input().split())
    G = [[] for i in range(N)]
    color = [0 for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    que = deque([0])
    color[0] = 1
    while len(que):
        p = que.popleft()
        for q in G[p]:
            if color[q] == 0:
                color[q] = -color[p]
                que.append(q)

    for i in range(Q):
        c, d = map(int, input().split())
        if color[c - 1] == color[d - 1]:
            print("Town")
        else:
            print("Road")


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
        input = """4 1
1 2
2 3
2 4
1 2"""
        output = """Road"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 2
2 3
3 4
4 5
1 3
1 5"""
        output = """Town
Town"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 9
2 3
5 6
4 8
8 9
4 5
3 4
1 9
3 7
7 9
2 5
2 6
4 6
2 4
5 8
7 8
3 6
5 6"""
        output = """Town
Road
Town
Town
Town
Town
Road
Road
Road"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
