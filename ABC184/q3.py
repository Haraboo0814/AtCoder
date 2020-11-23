import sys
from io import StringIO
import unittest


def resolve():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    r = r2 - r1
    c = c2 - c1
    if (r, c) == (0, 0):    # 移動なし
        ans = 0
    elif r == c or r == -c:     # 角
        ans = 1
    elif abs(r) + abs(c) <= 3:  # 近傍
        ans = 1
    elif (r ^ c ^ 1) & 1:   # パリティ
        ans = 2
    elif abs(r) + abs(c) <= 6:  # 近傍 → 近傍
        ans = 2
    elif abs(r + c) <= 3 or abs(r - c) <= 3:    # 角 → 近傍
        ans = 2
    else:       # max
        ans = 3
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
        input = """1 1
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
1 200001"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 3
998244353 998244853"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
