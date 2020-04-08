import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    abc = [chr(i) for i in range(97, 97 + n)]

    def dfs(s, idx):
        if len(s) == n:
            print(s)
        else:
            for i in range(idx + 1):
                if idx == i:
                    dfs(s + abc[i], idx + 1)
                else:
                    dfs(s + abc[i], idx)

    dfs("", 0)


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
        input = """1"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """aa
ab"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
