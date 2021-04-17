import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    ans = sorted(list(A ^ B))
    for a in ans:
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
        input = """2 2
1 2
1 3"""
        output = """2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 2 3 4
1 2 3 4"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
