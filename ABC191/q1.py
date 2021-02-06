import sys
from io import StringIO
import unittest


def resolve():
    v, t, s, d = map(int, input().split())
    mi = v * t
    ma = v * s
    if d < mi or ma < d:
        print("Yes")
    else:
        print("No")


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
        input = """10 3 5 20"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3 5 30"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
