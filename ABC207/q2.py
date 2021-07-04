import sys
from io import StringIO
import unittest
import math


def resolve():
    a, b, c, d = map(int, input().split())
    if (c * d - b) == 0:
        print(-1)
        return
    ans = math.ceil(a / (c * d - b))
    if ans < 0:
        print(-1)
    else:
        print(math.ceil(a / (c * d - b)))


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
        input = """5 2 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9 2 3"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
