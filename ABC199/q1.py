import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = map(int, input().split())
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")


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
        input = """2 2 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10 10"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 4 5"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
