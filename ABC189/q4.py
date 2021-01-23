import sys
from io import StringIO
import unittest

"""
https://atcoder.jp/contests/abc189/editorial/537
x0の場合から順に
"""


def resolve():
    n = int(input())
    f = 1
    for i in range(1, n + 1):
        s = input()
        if s[0] == "O":
            f += 2**(i)

    print(f)


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
        input = """2
AND
OR"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
OR
OR
OR
OR
OR"""
        output = """63"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
