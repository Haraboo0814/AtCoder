import sys
from io import StringIO
import unittest
import numpy as np


def resolve():
    x1, y1, x2, y2 = map(int, input().split())
    u = (x2 - x1, y2 - y1)
    u_rev = (x1 - x2, y1 - y2)
    # 回転行列
    R = np.array([[0, -1], [1, 0]])
    R_rev = np.array([[0, 1], [-1, 0]])

    u4 = np.dot(R, u)
    x4 = x1 + u4[0]
    y4 = y1 + u4[1]

    u3 = np.dot(R_rev, u_rev)
    x3 = x2 + u3[0]
    y3 = y2 + u3[1]

    print(x3, y3, x4, y4)


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
        input = """0 0 0 1"""
        output = """-1 1 -1 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 6 6"""
        output = """3 10 -1 7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31 -41 -59 26"""
        output = """-126 -64 -36 -131"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
