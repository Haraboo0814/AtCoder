import sys
from io import StringIO
import unittest


def resolve():
    import math
    a, b, h, m = map(int, input().split())
    a_deg = h / 12 * 360 + m / 60 * 30
    b_deg = m / 60 * 360
    print(math.sqrt(a**2 + b**2 - 2 * a * b *
                    math.cos(math.radians(min(360 - abs(a_deg - b_deg), abs(a_deg - b_deg))))))


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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
