import sys
from io import StringIO
import unittest


def resolve():
    from math import gcd
    T = int(input())
    for t in range(T):
        n, s, k = map(int, input().split())

        # 1. d = gcd(A, B, M) とし、
        # A, B, M をそれぞれ A/d, B/d, M/d に置き換える。
        d = gcd(n, gcd(s, k))
        n, s, k = n // d, s // d, k // d

        # 2. gcd(A, M) ≠ 1 のとき解なし
        if gcd(n, k) != 1:
            print(-1)

        # 3. gcd(A, M) = 1 のとき、modM における
        # A の逆元を A^−1 として、x = A^−1 * B が解
        # 逆元 : A^−1 = −q * r^−1 % P
        else:
            print(-s * pow(k, -1, n) % n)


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
        input = """4
10 4 3
1000 11 2
998244353 897581057 595591169
10000 6 14"""
        output = """2
-1
249561088
3571"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
