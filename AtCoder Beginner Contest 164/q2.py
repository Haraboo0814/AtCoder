import sys
from io import StringIO
import unittest


def resolve():
    A, B, C, D = map(int, input().split())
    while A > 0 and C > 0:
        C -= B
        if C <= 0:
            print("Yes")
            exit(0)
        A -= D
        if A <= D:
            print("No")
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
        input = """10 9 10 10"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """46 4 40 5"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
