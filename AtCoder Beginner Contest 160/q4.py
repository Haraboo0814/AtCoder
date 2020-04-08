import sys
from io import StringIO
import unittest


def resolve():
    n, x, y = map(int, input().split())
    ans = [0] * n
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            d = min(j - i, abs(i - x) + abs(j - y) + 1)
            ans[d] += 1

    for i in range(1, n):
        print(ans[i])


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
        input = """5 2 4"""
        output = """5\n4\n1\n0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 3"""
        output = """3\n0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 3 7"""
        output = """7\n8\n4\n2\n0\n0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4 8"""
        output = """10\n12\n10\n8\n4\n1\n0\n0\n0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
