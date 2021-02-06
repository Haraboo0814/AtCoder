import sys
from io import StringIO
import unittest


def resolve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    A_dash = filter(lambda a: a != x, A)
    for a in A_dash:
        print(a, end=" ")


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
        input = """5 5
3 5 6 5 4"""
        output = """3 6 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
3 3 3"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
