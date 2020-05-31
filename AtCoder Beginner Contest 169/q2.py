import sys
from io import StringIO
import unittest


def resolve():
    import numpy as np
    from decimal import Decimal

    n = int(input())
    A = np.array(list(map(Decimal, input().split())))
    if 0 in A:
        print(0)
        return

    a = Decimal(1)
    for b in A:
        a *= b
        if a > 10**18:
            print(-1)
            return
    print(a)


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
1000000000 1000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
101 9901 999999000001"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31
4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
