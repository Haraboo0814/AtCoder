import itertools
import sys
from io import StringIO
import unittest


def resolve():
    n, m, q = map(int, input().split())
    I = list(range(1, m + 1))
    A = list(map(list, itertools.combinations(I, n)))
    l = len(A)
    ans = [0 for i in range(l)]
    for _ in range(q):
        a, b, c, d = map(int, input().split())
        for i in range(l):
            if A[i][b - 1] - A[i][a - 1] == c:
                ans[i] += d

    print(max(ans))


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
        input = """3 4 3
1 3 3 100
1 2 2 10
2 3 2 10"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328"""
        output = """357500"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 1
1 10 9 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
