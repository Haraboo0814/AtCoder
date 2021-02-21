import sys
from io import StringIO
import unittest
import math


def resolve():
    k = int(input())
    ans = 0
    for i in range(1, k + 1):
        k_i = k / i
        for j in range(i, math.ceil(k_i) + 1):
            k_i_j = k_i / j
            for l in range(j, math.ceil(k_i_j) + 1):
                if i == j == l and i * j * l <= k:
                    ans += 1
                elif len(set([i, j, l])) == 2 and i * j * l <= k:
                    ans += 3
                elif i * j * l <= k:
                    ans += 6

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
        input = """2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10"""
        output = """53"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """31415"""
        output = """1937281"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
