import sys
from io import StringIO
import unittest


def resolve():
    x = int(input())
    c = 0
    while True:
        if x >= 500:
            x -= 500
            c += 1000
        elif x >= 5:
            x -= 5
            c += 5
        if x < 5:
            break
    print(c)


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
        input = """1024"""
        output = """2020"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000"""
        output = """2000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
