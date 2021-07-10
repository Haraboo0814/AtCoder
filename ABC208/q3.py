import sys
from io import StringIO
import unittest
from collections import defaultdict


def resolve():
    n, k = map(int, input().split())
    if n == 1:
        print(k)
        return
    A = list(map(int, input().split()))
    share = k // n
    d = defaultdict(int)
    B = sorted(A)
    k %= n
    if k == 0:
        for i in range(n):
            print(share)
        return

    for b in B:
        d[b] += 1
        k -= 1
        if k == 0:
            break
    for a in A:
        print(d[a] + share)


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
        input = """2 7
1 8"""
        output = """4
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 3
33"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 1000000000000
99 8 2 4 43 5 3"""
        output = """142857142857
142857142857
142857142858
142857142857
142857142857
142857142857
142857142857"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
