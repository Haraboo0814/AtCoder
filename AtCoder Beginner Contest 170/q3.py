import sys
from io import StringIO
import unittest


import numpy as np


def resolve():
    x, n = map(int, input().split())
    if n == 0:
        print(x)
        return
    P = set(map(int, input().split()))
    if x not in P:
        print(x)
        return

    P_not = np.array(list(set(list(range(-1, 102))) - P))
    diff = np.abs(P_not - x)
    print(P_not[diff.argmin()])


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
        input = """6 5
4 7 10 6 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 5
4 7 10 6 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 0"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
