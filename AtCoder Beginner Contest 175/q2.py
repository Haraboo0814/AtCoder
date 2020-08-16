import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    L = sorted(list(map(int, input().split())))
    cnt = 0
    checker = [[[0 for i in range(n)] for j in range(n)] for k in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i < j < k) and (L[i] != L[j] and L[i] != L[k] and L[j] != L[k]) and L[i] + L[j] > L[k]:
                    cnt += 1

    print(cnt)


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
4 4 9 7 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
4 5 4 3 3 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
9 4 6 1 9 6 10 6 6 8"""
        output = """39"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
