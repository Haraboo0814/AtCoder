import sys
from io import StringIO
import unittest


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    s = []
    ord = [-1 for i in range(n + 1)]
    rep = 1
    pos = 1
    while ord[pos] == -1:
        ord[pos] = len(s)
        s.append(pos)
        pos = A[pos - 1]
        rep += 1

    rep = len(s) - ord[pos]
    # l: ループが始まる点
    l = ord[pos]
    if k < l:
        print(s[k])
    else:
        # ループが始まるまでずらす
        k -= l
        k %= rep
        print(s[l + k])


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
        input = """4 5
3 2 4 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
