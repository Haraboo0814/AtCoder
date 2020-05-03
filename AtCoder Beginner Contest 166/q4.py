import sys
from io import StringIO
import unittest


def resolve():
    x = int(input())
    for i in range(-118, 120):
        for j in range(-119, 119):
            if i**5 - j**5 == x:
                print(i, j)
                exit(0)


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
        input = """6
2 3 3 1 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 2 4 2 8 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
