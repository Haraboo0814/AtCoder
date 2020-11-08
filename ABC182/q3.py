import sys
from io import StringIO
import unittest


def resolve():
    n = list(map(int, list(input())))
    sum_n = sum(n)
    if sum_n % 3 == 0:
        print(0)
        return
    elif len(n) == 1:
        print(-1)
        return
    elif sum_n % 3 == 1:
        for i in range(1, 10, 3):
            if i in n:
                print(1)
                return
    elif sum_n % 3 == 2:
        for i in range(2, 10, 3):
            if i in n:
                print(1)
                return
    if len(n) > 2:
        print(2)
    else:
        print(-1)


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
        input = """35"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """369"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6227384"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
