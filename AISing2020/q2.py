import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, n + 1):
        if i % 2 != 0 and A[i - 1] % 2 != 0:
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
        input = """5
1 3 4 5 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15
13 76 46 15 50 98 93 77 31 43 84 90 6 24 14"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
