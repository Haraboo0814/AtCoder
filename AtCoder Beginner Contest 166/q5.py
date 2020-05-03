import sys
from io import StringIO
import unittest


def resolve():
    from collections import Counter

    n = int(input())
    A = list(map(int, input().split()))
    B = [i + A[i - 1] for i in range(1, n + 1)]
    C = Counter(B)
    ans = 0
    for i in range(1, n + 1):
        x = i - A[i - 1]
        if x in C.keys():
            ans += C[x]
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
2 3 3 1 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
5 2 4 2 8 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """32
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5"""
        output = """22"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
