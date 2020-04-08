import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    dA = {}
    A = []
    for a in input().split():
        A.append(a)
        if a in dA:
            dA[a] += 1
        else:
            dA[a] = 1

    cA = {}
    for a in dA:
        cA[a] = dA[a] * (dA[a] - 1) // 2

    s = sum(cA.values())
    for a in A:
        print(s - dA[a] + 1)


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
        input = """5\n1 1 2 1 2"""
        output = """2\n2\n3\n2\n3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4\n1 2 3 4"""
        output = """0\n0\n0\n0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5\n3 3 3 3 3"""
        output = """6\n6\n6\n6\n6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8\n1 2 1 4 2 1 4 1"""
        output = """5\n7\n5\n7\n7\n5\n7\n5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
