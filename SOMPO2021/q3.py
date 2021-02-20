import sys
from io import StringIO
import unittest


def resolve():
    a, k = map(int, input().split())
    for _ in range(k):
        a = upper(a) - lower(a)
        if a == 0:
            print(0)
            return

    print(a)


def upper(a):
    a = list(str(a))
    a.sort(reverse=True)
    a = int("".join(a))
    return a


def lower(a):
    a = [c for c in list(str(a)) if c != "0"]
    a.sort()
    a = int("".join(a))
    return a


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
        input = """314 2"""
        output = """693"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6174 100000"""
        output = """6174"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
