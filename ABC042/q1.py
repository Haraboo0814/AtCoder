import sys
from io import StringIO
import unittest


def resolve():
    A = sorted(list(map(int, input().split())))
    if A[0] == 5 and A[1] == 5 and A[2] == 7:
        print("YES")
    else:
        print("NO")


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
        input = """5 5 7"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7 5"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
