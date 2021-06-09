import sys
from io import StringIO
import unittest


def resolve():
    x, y = map(int, input().split())
    if (x == 0 and y == 1) or (x == 1 and y == 0) or (x == 2 and y == 2):
        print(2)
    elif (x == 0 and y == 2) or (x == 2 and y == 0) or (x == 1 and y == 1):
        print(1)
    elif (x == 2 and y == 1) or (x == 1 and y == 2) or (x == 0 and y == 0):
        print(0)


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
        input = """0 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
