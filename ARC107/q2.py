import sys
from io import StringIO
import unittest

# 式化


def f(n, k):
    return min(k - 1, 2 * n - k + 1)


def resolve():
    n, k = map(int, input().split())
    k = abs(k)
    ans = 0
    for x in range(2 + k, 2 * n + 1):
        ans += f(n, x) * f(n, x - k)
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
        input = """2 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2525 -425"""
        output = """10314607400"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
