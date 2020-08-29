import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    M = max(A) + 1
    C = [0 for i in range(M)]
    for a in A:
        C[a] += 1

    pairwise = True
    for i in range(2, M):
        cnt = 0
        for j in range(i, M, i):
            cnt += C[j]

        if cnt > 1:
            pairwise = False

    if pairwise:
        print("pairwise coprime")
        return

    g = 0
    for i in range(n):
        g = math.gcd(g, A[i])

    if g == 1:
        print("setwise coprime")
        return

    print("not coprime")


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
        input = """3
3 4 5"""
        output = """pairwise coprime"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
6 10 15"""
        output = """setwise coprime"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
6 10 16"""
        output = """not coprime"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
