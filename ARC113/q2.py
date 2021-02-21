import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = map(int, input().split())
    c %= 4
    if c == 0:
        c = 4
    b_c = b**c % 100 % 4
    if b_c == 0:
        b_c = 4
    a %= 10
    print(a**b_c % 10)


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
        input = """4 3 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3141592 6535897 9323846"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
