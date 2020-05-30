import sys
from io import StringIO
import unittest


def resolve():
    h1, m1, h2, m2, k = map(int, input().split())
    h = h2 - h1
    if h < 0:
        h += 24
    m = m2 - m1
    if m < 0:
        m += 60
        h -= 1

    print(h * 60 + m - k)


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
        input = """10 0 15 0 30"""
        output = """270"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 0 12 0 120"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
