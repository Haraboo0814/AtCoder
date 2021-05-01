import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    print(s.count("ZONe"))


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
        input = """abcdZONefghi"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ZONeZONeZONe"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """helloAtZoner"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
