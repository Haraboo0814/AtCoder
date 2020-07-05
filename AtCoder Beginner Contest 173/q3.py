import sys
from io import StringIO
import unittest


def resolve():
    import numpy as np
    import itertools
    import copy

    H, W, K = map(int, input().split())
    table = []
    for _ in range(H):
        s = list(input())
        table.append(s)

    ans = 0
    for i in range(2**H):
        mask_h = format(i, '0{}b'.format(H))
        for j in range(2**W):
            mask_w = format(j, '0{}b'.format(W))
            black = 0
            for di in range(H):
                for dj in range(W):
                    if mask_h[di] == '0' and mask_w[dj] == '0' and table[di][dj] == "#":
                        black += 1
            if black == K:
                ans += 1
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
        input = """2 3 2
..#
###"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 4
..#
###"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 3
##
##"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6 6 8
..##..
.#..#.
#....#
######
#....#
#....#"""
        output = """208"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
