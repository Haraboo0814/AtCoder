import sys
from io import StringIO
import unittest
import numpy as np


def resolve():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    A = np.array(sorted(list(map(int, input().split()))))
    if A[0] != 1:
        A = np.insert(A, 0, 0)
    if A[-1] != n:
        A = np.insert(A, len(A), n + 1)
    d = np.diff(A, 1) - 1
    d = d[d > 0]
    k = np.min(d)
    ans = np.sum(np.ceil(d / k))
    print(int(ans))


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
        input = """5 2
1 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 3
13 3 9"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
5 2 1 4 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 0"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
