import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    C = 1000
    kabu = 0

    for i in range(1, n):
        if A[i - 1] <= A[i]:
            kabu = C // A[i - 1]
            C += kabu * (A[i] - A[i - 1])

    print(C)


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
        input = """7
100 130 130 130 115 115 150"""
        output = """1685"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
200 180 160 140 120 100"""
        output = """1000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
157 193"""
        output = """1216"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
