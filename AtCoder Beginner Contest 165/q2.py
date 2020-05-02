import sys
from io import StringIO
import unittest


def resolve():
    import math

    x = int(input())
    a = 100
    i = 0
    c = 0
    while True:
        c += 1
        i = a * 0.01
        a = int(a + i)
        if a >= x:
            print(c)
            exit(0)


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
        input = """103"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000000000000"""
        output = """3760"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1333333333"""
        output = """1706"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
