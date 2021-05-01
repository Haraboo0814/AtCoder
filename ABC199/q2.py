import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maA = max(A)
    miB = min(B)
    if miB < maA:
        print(0)
        return

    print(len(list(range(maA, miB + 1))))


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
        input = """2
3 2
7 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 5 3
10 7 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
3 2 5
6 9 8"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
