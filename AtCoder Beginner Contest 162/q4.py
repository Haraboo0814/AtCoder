import sys
from io import StringIO
import unittest


def resolve():
    import math

    n = int(input())
    s = input()
    d = 0
    for i in range(1, math.ceil(n / 2)):
        for j in range(i, n - i):
            if s[j - i] != s[j] and s[j] != s[j + i] and s[j - i] != s[j + i]:
                d += 1
    print(s.count('R') * s.count('G') * s.count('B') - d)


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
        input = """4\nRRGB"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """39\nRBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
