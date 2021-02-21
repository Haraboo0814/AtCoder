import sys
from io import StringIO
import unittest


def resolve():
    s = list(input())[::-1]
    d = {}
    ans = 0
    for i in range(len(s) - 1):
        c = s[i]
        d.setdefault(c, 0)
        d[c] += 1
        if c == s[i + 1]:
            ans += i - d[c] + 1
            d = {c: i + 1}

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
        input = """accept"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoder"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """anerroroccurred"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
