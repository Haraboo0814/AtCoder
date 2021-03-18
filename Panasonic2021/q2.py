import sys
from io import StringIO
import unittest
import math


def resolve():
    a, b, w = map(int, input().split())
    w *= 1000

    ma = math.floor(w / a)
    mi = math.ceil(w / b)
    if ma < mi:
        ma, mi = -1, -1

    if mi != 10**18 and ma != -1:
        print(mi, ma)
    else:
        print("UNSATISFIABLE")


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
        input = """100 200 2"""
        output = """10 20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """120 150 2"""
        output = """14 16"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """300 333 1"""
        output = """UNSATISFIABLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
