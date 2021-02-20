import sys
from io import StringIO
import unittest


def resolve():
    x = int(input())
    c = x % 100
    print(100 - c)


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
        input = """140"""
        output = """60"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
