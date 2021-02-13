import sys
from io import StringIO
import unittest


"""
https://atcoder.jp/contests/arc112/editorial/725
"""


def resolve():
    b, c = map(int, input().split())
    l = b - c // 2
    r = b
    if c >= 2:
        r = b + (c - 2) // 2

    b = -b
    c -= 1
    p = b - c // 2
    q = b + c // 2
    ans = r - l + 1 + q - p + 1
    u = max(l, p)
    v = min(r, q)

    if u <= v:
        ans -= v-u+1

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
        input = """11 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """112 20210213"""
        output = """20210436"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """-211 1000000000000000000"""
        output = """1000000000000000422"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
