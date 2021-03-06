import sys
from io import StringIO
import unittest
import numpy as np


"""
式変形
"""


def resolve():
    n = int(input())
    A = np.asarray(list(map(int, input().split())))
    print(n * sum(A**2) - sum(A)**2)


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
2 8 4"""
        output = """56"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-5 8 9 -4 -3"""
        output = """950"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
