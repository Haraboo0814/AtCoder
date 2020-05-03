import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    if n % 2 != 0:
        for i in range(m):
            print(i + 1, n - i)
    else:
        for i in range(m):
            if i < m / 2:
                print(i + 1, n - i)
            else:
                print(i + 1, n - i - 1)


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
        input = """4 1"""
        output = """2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3"""
        output = """1 6
2 5
3 4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
