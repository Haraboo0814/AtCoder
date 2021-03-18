import sys
from io import StringIO
import unittest


"""
x桁のカンマごとにみる
"""


def resolve():
    n = int(input())
    ans = 0

    if n >= 1000:
        ans += n-999
    if n >= 1000000:
        ans += n-999999
    if n >= 1000000000:
        ans += n-999999999
    if n >= 1000000000000:
        ans += n-999999999999
    if n >= 1000000000000000:
        ans += n-999999999999999

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
        input = """1010"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27182818284590"""
        output = """107730272137364"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
