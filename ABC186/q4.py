import sys
from io import StringIO
import unittest

"""
Σ^(N-1)_(i=1) Σ^N_(j=i+1) A_j - A_i
 = Σ^N_(j=i+1) A_j - (n - i)A_i

"""


def resolve():
    import numpy as np

    n = int(input())
    A = sorted(list(map(int, input().split())))
    c = np.cumsum(A)
    s = c[-1]
    ans = 0

    for i in range(n - 1):
        # Σ^N_(j=i+1) A_j - (n - i)A_i
        ans += s - c[i] - (n - (i + 1)) * A[i]

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
        input = """3
5 1 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
31 41 59 26 53"""
        output = """176"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
