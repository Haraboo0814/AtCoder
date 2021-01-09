import sys
from io import StringIO
import unittest

# https://atcoder.jp/contests/arc111/editorial/491


def resolve():
    n, m = map(int, input().split())
    print(pow(10, n, m * m) // m % m)


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
        input = """1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 7"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 9997"""
        output = """9015"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
