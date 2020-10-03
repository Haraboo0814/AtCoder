import sys
from io import StringIO
import unittest


def resolve():
    n, s = input().split()
    n = int(n)
    ans = 0
    for i in range(n):
        c1 = 0
        c2 = 0
        for c in s[i:]:
            if c == "A":
                c1 += 1
            elif c == "T":
                c1 -= 1
            elif c == "C":
                c2 += 1
            else:
                c2 -= 1
            if c1 == 0 and c2 == 0:
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
        input = """4 AGCT"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 ATAT"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 AAATACCGCG"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
