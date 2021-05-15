import sys
from io import StringIO
import unittest
import numpy as np
import collections


def resolve():
    n = int(input())
    A = np.array(list(map(int, input().split())))
    A %= 200
    ans = 0
    c = collections.Counter(A)
    for cnt in c.values():
        if cnt > 1:
            ans += (cnt * (cnt - 1)) // 2

    print(ans)


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
        input = """6
123 223 123 523 200 2000"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
199 100 200 400 300 500 600 200"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
