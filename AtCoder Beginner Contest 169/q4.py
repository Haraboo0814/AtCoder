import sys
from io import StringIO
import unittest


def resolve():
    import math

    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    n = int(input())
    p = prime_factorize(n)
    if len(p) == 0:
        print(0)
        return

    pn = list(set(p))
    ans = 0
    for m in pn:    # 素数ごとに数え上げる
        i = 1
        k = p.count(m)
        while(k > 0):
            k -= i
            i += 1
            if k >= 0:
                ans += 1
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
        input = """24"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """64"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000007"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """997764507000"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
