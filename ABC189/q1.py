import sys
from io import StringIO
import unittest


def resolve():
    s = list(input())
    if len(list(set(s))) == 1:
        print("Won")
    else:
        print("Lost")


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
        input = """SSS"""
        output = """Won"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """WVW"""
        output = """Lost"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
