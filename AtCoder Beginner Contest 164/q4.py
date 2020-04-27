import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    l = len(s)
    dp = [0 for i in range(2019)]
    dp[0] = 1

    r = 0
    for i in range(1, l + 1):
        r += int(s[-i]) * pow(10, i - 1, 2019)
        r %= 2019
        dp[r] += 1

    print(sum([(i * (i - 1)) // 2 for i in dp]))


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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
