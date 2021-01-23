import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    stack = []
    ma = 0
    for i, a in enumerate(A):
        if len(stack) == 0:
            stack.append((a, i))
        elif stack[-1][0] == a:
            continue
        elif stack[-1][0] < a:
            stack.append((a, i))
        else:
            last_pos = 0
            while len(stack) > 0 and stack[-1][0] > a:
                aj, ij = stack[-1]
                stack.pop(-1)
                area = aj * (i - ij)
                ma = max(ma, area)
                last_pos = ij
            stack.append((a, last_pos))

    while len(stack) > 0:
        aj, ij = stack[-1]
        stack.pop(-1)
        area = aj * (n - ij)
        ma = max(ma, area)

    print(ma)


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
2 4 4 9 4 9"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
200 4 4 9 4 9"""
        output = """200"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
