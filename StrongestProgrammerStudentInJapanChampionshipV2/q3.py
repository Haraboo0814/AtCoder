import sys
from io import StringIO
import unittest
import math


def resolve():
    a, b = map(int, input().split())
    for i in range(b - a, 0, -1):
        x = i * math.ceil(a / i)
        y = x + i
        if b >= y:
            print(i)
            return

    print(1)


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
        input = """2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """199999 200000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """101 139"""
        output = """34"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
