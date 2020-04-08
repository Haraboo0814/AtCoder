import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    ans = 0
    for a in A:
        if a >= S / (4 * m):
            ans += 1

    if ans >= m:
        print("Yes")
    else:
        print("No")


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
        input = """4 1\n5 4 2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2\n380 19 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 3\n4 56 78 901 2 345 67 890 123 45 6 789"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
