import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    H = list(map(int, input().split()))
    K = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        K[a - 1].append(H[b - 1])
        K[b - 1].append(H[a - 1])
    ans = 0
    for i in range(n):
        for k in K:
            if len(k) != 0 and H[i] > max(k):
                ans += 1
            elif len(k) == 0:
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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
