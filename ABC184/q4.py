import sys
from io import StringIO
import unittest


def resolve():
    dp = [[[-1 for i in range(101)] for j in range(101)] for k in range(101)]

    def f(a, b, c):
        if dp[a][b][c] != -1:
            return dp[a][b][c]

        if a == 100 or b == 100 or c == 100:
            return 0

        ans = 0
        ans += (f(a + 1, b, c) + 1) * a / (a + b + c)
        ans += (f(a, b + 1, c) + 1) * b / (a + b + c)
        ans += (f(a, b, c + 1) + 1) * c / (a + b + c)
        dp[a][b][c] = ans
        return ans

    a, b, c = map(int, input().split())
    print(f(a, b, c))


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
        input = """99 99 99"""
        output = """1.000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """98 99 99"""
        output = """1.331081081"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 0 1"""
        output = """99.000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """31 41 59"""
        output = """91.835008202"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
