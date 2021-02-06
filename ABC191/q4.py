import sys
from io import StringIO
import unittest
import math
from decimal import Decimal


def resolve():
    x, y, r = map(Decimal, input().split())
    min_x = math.ceil(x - r)
    max_x = math.floor(x + r)
    ans = 0
    for i in range(min_x, max_x + 1):
        p = Decimal.sqrt(r**2 - (x - Decimal(i))**2)
        min_y = math.ceil(y - p)
        max_y = math.floor(y + p)
        ans += max_y - min_y + 1

    print(ans)


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
        input = """0.2 0.8 1.1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 100 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """42782.4720 31949.0192 99999.99"""
        output = """31415920098"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
