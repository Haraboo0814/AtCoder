import sys
from io import StringIO
import unittest


def resolve():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n) + "200")

    print(n)


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
        input = """2021 4"""
        output = """50531"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """40000 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8691 20"""
        output = """84875488281"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
