import sys
from io import StringIO
import unittest


def resolve():
    t = input()
    s = ""
    for c in t:
        if c == "?":
            c = "D"

        s += c
    print(s)


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
        input = """PD?D??P"""
        output = """PDPDPDP"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """P?P?"""
        output = """PDPD"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
