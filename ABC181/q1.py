import sys
from io import StringIO
import unittest


def resolve():
    if int(input()) % 2 == 0:
        print("White")
    else:
        print("Black")

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
        input = """2"""
        output = """White"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """Black"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
