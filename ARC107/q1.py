import sys
from io import StringIO
import unittest


def resolve():
    from decimal import Decimal
    m = Decimal(998244353)
    a, b, c = map(Decimal, input().split())
    A = a*(a+1)/2 % m
    B = b*(b+1)/2 % m
    C = c*(c+1)/2 % m

    print((A*B*C) % m)


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
        input = """1 2 3"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 987654321 123456789"""
        output = """951633476"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
