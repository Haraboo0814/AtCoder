import sys
from io import StringIO
import unittest


def resolve():
    a, b = map(int, input().split())
    print((1. - b / a) * 100)


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
        input = """100 80"""
        output = """20.0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 6"""
        output = """14.285714285714285714"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99999 99998"""
        output = """0.00100001000010000100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
