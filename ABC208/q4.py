import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    d = [[1 << 60] * n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        d[a - 1][b - 1] = c

    ans = 0
    # ワーシャル・フロイド法
    for k in range(n):
        nxt = [[0] * n for l in range(n)]
        for i in range(n):
            for j in range(n):
                nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
                if nxt[i][j] < 1 << 59:
                    ans += nxt[i][j]
        d = nxt

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
        input = """3 2
1 2 3
2 3 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 20
1 2 6
1 3 10
1 4 4
1 5 1
2 1 5
2 3 9
2 4 8
2 5 6
3 1 5
3 2 1
3 4 7
3 5 9
4 1 4
4 2 6
4 3 4
4 5 8
5 1 2
5 2 5
5 3 6
5 4 5"""
        output = """517"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
