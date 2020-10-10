import sys
from io import StringIO
import unittest


'''
場合分け
ans : 赤い正方形の内部と青い正方形の内部が重ならないように置く方法の数は複雑そうなので、
全体から赤い正方形の内部と青い正方形の内部が重なるように置く方法(X1と呼ぶことにする)
を引いて求めよう
ans = (N - A + 1)**2 * (N - B + 1)**2 - X1

X1 :「赤い正方形の内部と青い正方形の内部が重なる」には、「赤い正方形のx座標の範囲と
青い正方形のx座標の範囲が重なる」「赤い正方形のy座標の範囲と青い正方形の
y座標の範囲が重なる」が両方成り立っている必要がある。
対称性からこれらはどちらも同じ値(X2と呼ぶことにする) で、
X1 = X2**2

X2 : 長さAの区間と長さBの区間を長さNの区間に詰めた時に重なる方法の数。
区間の置き方の数から区間が重ならない置き方の総数(X3と呼ぶことにする)を引けば、
X2 = (N - A + 1) * (N - B + 1) - X3
と求められそう

X3 : 対称性より赤が左にあるパターンと青が左にあるパターンに分けて良い。
赤が左にあるパターンの総数をX4とすると、
X3 = 2 * X4

X4 : それぞれ (空白)(赤)(空白)(青)(空白) みたいなパターンになって空白のマスの総数は 
N - A - B だから N - A - B < 0 なら X4 = 0通りだし、 
N - A - B ≥ 0 なら X4 = (N - A - B + 2) * (N - A - B + 1) / 2
通りある
'''


def resolve():
    T = int(input())
    for t in range(T):
        N, A, B = map(int, input().split())
        if N - A - B < 0:
            X4 = 0
        else:
            X4 = (N - A - B + 2) * (N - A - B + 1) // 2
        X3 = 2 * X4
        X2 = (N - A + 1) * (N - B + 1) - X3
        X1 = X2**2
        ans = (N - A + 1)**2 * (N - B + 1)**2 - X1
        print(ans % (10**9 + 7))


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
3 1 2
4 2 2
331895368 154715807 13941326"""
        output = """20
32
409369707"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
