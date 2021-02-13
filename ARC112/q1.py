import sys
from io import StringIO
import unittest


def resolve():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        c = max(0, r - l - (l - 1))
        ans = int(c / 2 * (2 + (c - 1)))
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
        input = """5
2 6
0 0
1000000 1000000
12345 67890
0 1000000"""
        output = """6
1
0
933184801
500001500001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
