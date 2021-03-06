import sys
from io import StringIO
import unittest
import numpy as np


def resolve():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A = np.asarray(A)
    B = np.asarray(B)
    A_idx = A.argsort()
    B_idx = B.argsort()
    if A_idx[0] != B_idx[0]:
        print(max(A[A_idx[0]], B[B_idx[0]]))
    else:
        print(min(A[A_idx[0]] + B[B_idx[0]],
            max(A[A_idx[0]], B[B_idx[1]]),
            max(A[A_idx[1]], B[B_idx[0]])))


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
8 5
4 4
7 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
11 7
3 2
6 7"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
