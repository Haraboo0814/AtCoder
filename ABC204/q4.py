import sys
from io import StringIO
import unittest
import numpy as np


def resolve():
    n = int(input())
    T = list(map(int, input().split()))
    S = np.sum(T)
    dp = np.zeros(S // 2 + 1, dtype=np.bool)
    dp[-1] = 1
    for i in range(n):
        if S // 2 + 1 - T[i] < 0:
            continue
        dp[:S // 2 + 1 - T[i]] |= dp[T[i]:]  # numpyを用いていっぺんに遷移

    print(S - S//2 + np.argmax(dp))


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
        input = """5
8 3 7 2 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1000 1"""
        output = """1000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
3 14 15 9 26 5 35 89 79"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
