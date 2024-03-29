import sys
from io import StringIO
import unittest
import math


def resolve():
    r, x, y = map(int, input().split())
    dist = x**2 + y**2
    if r**2 > dist:
        print(2)
    else:
        print(math.ceil(math.sqrt(dist / r**2)))


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
        input = """5 15 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 11 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 4 4"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
