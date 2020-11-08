import sys
from io import StringIO
import unittest


def cumsum(xs):
    '''
    累積和Pと、それまでの累積和の最大値Q
    '''
    P = [xs[0]]
    Q = [xs[0]]
    for x in xs[1:]:
        P.append(P[-1] + x)
        Q.append(max(Q[-1], P[-1]))
    return P, Q


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    P, Q = cumsum(A)
    # P[i]: 動作iの合計の座標の変化
    # Q[i]: 動作iを座標0で始めた場合の、開始から終了までの座標の最大値
    ans = 0
    x = 0
    for i in range(n):
        # 動作iでの座標のmax = x + Q[i]
        # 答えとなる最大値を保存
        ans = max(ans, x + Q[i])
        # 座標の更新
        x = x + P[i]

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
        input = """3
2 -1 -2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-2 1 3 -1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
-1000 -1000 -1000 -1000 -1000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
