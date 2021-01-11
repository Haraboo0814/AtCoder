import sys
from io import StringIO
import unittest
import numpy as np
import math
import copy


def resolve():
    n = int(input())
    A = np.array(list(map(int, input().split())))
    b = copy.deepcopy(A)
    b1 = A[::2]
    b2 = A[1::2]
    while len(b) > 2:
        b = np.maximum(b1, b2)
        b1 = b[::2]
        b2 = b[1::2]

    print(np.where(A == np.min(b))[0][0] + 1)


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
1 4 2 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3 1 5 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
6 13 12 5 3 7 10 11 16 9 8 15 2 1 14 4"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
