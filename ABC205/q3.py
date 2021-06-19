import sys
from io import StringIO
import unittest


def resolve():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        if a**2 > b**2:
            print(">")
        elif a**2 < b**2:
            print("<")
        else:
            print("=")
    else:
        if a**3 > b**3:
            print(">")
        elif a**3 < b**3:
            print("<")
        else:
            print("=")


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
        input = """3 2 4"""
        output = """>"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-7 7 2"""
        output = """="""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-8 6 3"""
        output = """<"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
