import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    t = input()
    if s == 'Y':
        print(t.upper())
    else:
        print(t)


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
        input = """Y
a"""
        output = """A"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """N
b"""
        output = """b"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
