import sys
from io import StringIO
import unittest


def resolve():
    x, y, a, b = map(int, input().split())
    if x * a >= x + b:
        print((y - 1 - x) // b)
    else:
        ex = 0
        while x * a < x + b and x < y:
            x *= a
            ex += 1

        print(ex + (y - 1 - x) // b)


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
        input = """4 20 2 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1000000000000000000 10 1000000000"""
        output = """1000000007"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
