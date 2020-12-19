import sys
from io import StringIO
import unittest


def resolve():
    import numpy as np
    h, w = map(int, input().split())
    A = []
    for _ in range(h):
        A.append(list(map(int, input().split())))
    A = np.asarray(A)
    mi = np.min(A)
    print(int(np.sum((A - mi))))


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
        input = """2 3
2 2 3
3 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
99 99 99
99 0 99
99 99 99"""
        output = """792"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
4 4
4 4
4 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
