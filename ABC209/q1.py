import sys
from io import StringIO
import unittest


def resolve():
    a, b = map(int, input().split())
    print(len(list(range(a, b + 1))))


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
        input = """2 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 100"""
        output = """91"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
