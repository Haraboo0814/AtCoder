import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A, B = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)


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
        input = """5\n1 2\n1 3\n3 4\n3 5"""
        output = """1 2 5 4 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
