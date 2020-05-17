import sys
from io import StringIO
import unittest


def resolve():
    from math import gcd
    from collections import defaultdict
    MOD = 1000000007

    N = int(input())

    d = defaultdict(int)
    zeros = 0
    for i in range(N):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            zeros += 1
        else:
            g = gcd(a, b)
            a //= g
            b //= g
            if a < 0:
                a *= -1
                b *= -1
            if a == 0 and b == -1:
                b = 1
            d[(a, b)] += 1

    ans = 1
    free = 0
    for (a, b), n in d.items():
        if b > 0:
            if (b, -a) in d:
                m = d[(b, -a)]
                ans = ans * (pow(2, n, MOD) + pow(2, m, MOD) - 1) % MOD
            else:
                free += n
        else:
            if (-b, a) not in d:
                free += n

    ans = (ans * pow(2, free, MOD) + zeros - 1) % MOD
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
1 2
-1 1
2 -1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
3 2
3 2
-1 1
2 -1
-3 -9
-8 12
7 7
8 1
8 2
8 4"""
        output = """479"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
