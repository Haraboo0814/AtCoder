import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    R, B = [], []
    for _ in range(n):
        x, c = input().split()
        if c == "R":
            R.append(int(x))
        else:
            B.append(int(x))
    R.sort()
    B.sort()
    for r in R:
        print(r)
    for b in B:
        print(b)


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
        input = """4\n10 B\n6 R\n2 R\n4 B"""
        output = """2\n6\n4\n10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2\n5 B\n7 B"""
        output = """5\n7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
