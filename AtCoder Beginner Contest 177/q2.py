import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    t = input()
    ans = 10**18
    for i in range(len(s) - len(t) + 1):
        a = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                a += 1
        if ans > a:
            ans = a

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
        input = """cabacc
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """codeforces
atcoder"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
