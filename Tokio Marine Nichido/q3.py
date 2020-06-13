import sys
from io import StringIO
import unittest


from numba import jit
import numpy as np


@jit
def resolve():
    n, k = map(int, input().split())
    A = np.array(list(map(int, input().split())), dtype=np.int64)
    for m in range(k):
        B = np.zeros(n + 1, dtype=np.int64)
        for i in range(n):
            l = max(0, i - A[i])
            r = min(n, i + A[i] + 1)
            B[l] += 1
            if r < n:
                B[r] -= 1
        A = np.cumsum(B)[:-1]
        if np.all(A == n):
            break

    for a in A:
        print(a, end=" ")


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
        input = """5 1
1 0 0 1 0"""
        output = """1 2 2 1 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
1 0 0 1 0"""
        output = """3 3 4 4 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
