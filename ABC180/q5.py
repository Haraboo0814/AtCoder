import sys
from io import StringIO
import unittest
from numba import njit
import numpy as np

INF = 1001001001

'''
bitDP
numbaは内包表記は使えない
'''


@njit
def bit_dp(n, n2, dp, dist):
    for i in range(n2):
        for j in range(n):
            if ~i << j & 1:
                continue
            for k in range(n):
                if i >> k & 1:
                    continue
                dp[i | 1 << k][k] = min(
                    dp[i | 1 << k][k], dp[i][j] + dist[j][k])

    return dp[n2 - 1][0]


def resolve():
    n = int(input())
    X, Y, Z = [], [], []
    for _ in range(n):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)

    n2 = 1 << n
    dp = np.full((1 << n, n), INF, np.int64)
    dist = np.full((n, n), INF, np.int64)
    for i in range(n):
        for j in range(n):
            now = abs(X[i] - X[j])
            now += abs(Y[i] - Y[j])
            now += max(0, Z[j] - Z[i])
            dist[i][j] = now

    for i in range(n):
        if i != 0:
            dp[1 << i][i] = dist[0][i]

    print(bit_dp(n, n2, dp, dist))


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
        input = """2
0 0 0
1 2 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
0 0 0
1 1 1
-1 -1 -1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """17
14142 13562 373095
-17320 508075 68877
223606 -79774 9979
-24494 -89742 783178
26457 513110 -64591
-282842 7124 -74619
31622 -77660 -168379
-33166 -24790 -3554
346410 16151 37755
-36055 51275 463989
37416 -573867 73941
-3872 -983346 207417
412310 56256 -17661
-42426 40687 -119285
43588 -989435 -40674
-447213 -59549 -99579
45825 7569 45584"""
        output = """6519344"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
