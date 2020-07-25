import sys
from io import StringIO
import unittest


def resolve():
    import numpy as np
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = np.cumprod(np.array(A))

    for i in range(n - k):
        if A[i] < A[k + i]:
            print("Yes")
        else:
            print("No")


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
        input = """5 3
96 98 95 100 20"""
        output = """Yes
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
1001 869120 1001"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 7
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9"""
        output = """Yes
Yes
No
Yes
Yes
No
Yes
Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
