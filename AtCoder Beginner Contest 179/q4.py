import sys
from io import StringIO
import unittest


def resolve():
    n, k = map(int, input().split())
    S = []
    L, R = [], []
    for _ in range(k):
        l1, r1 = map(int, input().split())
        L.append(l1)
        R.append(r1)

    dp = [0 for i in range(n + 1)]
    dpsum = [0 for i in range(n + 1)]
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            Li = i - R[j]
            Ri = i - L[j]
            if Ri < 0:
                continue
            Li = max(1, Li)
            dp[i] += dpsum[Ri] - dpsum[Li - 1]  # dp[Li] ~ dp[Ri]

        dpsum[i] = dpsum[i - 1] + dp[i]

    print(dp[n] % 998244353)


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
        input = """5 2
1 1
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
3 3
5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """60 3
5 8
1 3
10 15"""
        output = """221823067"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
