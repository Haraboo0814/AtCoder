import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = map(int, input().split())
    if c == 1:
        a, b = b, a

    if a <= b:
        if c == 0:
            print("Aoki")
        else:
            print("Takahashi")

    else:
        if c == 0:
            print("Takahashi")
        else:
            print("Aoki")


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
        input = """2 1 0"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 0"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1"""
        output = """Takahashi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
