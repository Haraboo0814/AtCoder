import sys
from io import StringIO
import unittest


def resolve():
    import itertools

    a1, a2, a3 = map(int, input().split())
    n = a1 + a2 + a3
    l = list(range(1, n + 1))
    P = list(map(list, itertools.permutations(l)))
    c = 0
    for p in P:
        p1, p2, p3 = p[:a1], p[a1:a1 + a2], p[a1 + a2:]
        flag = 0
        for i in range(a1 - 1):
            if p1[i] > p1[i + 1]:
                flag = 1
        for i in range(a2 - 1):
            if p2[i] > p2[i + 1]:
                flag = 1
        for i in range(a3 - 1):
            if p3[i] > p3[i + 1]:
                flag = 1
        for i in range(a2):
            if p1[i] > p2[i]:
                flag = 1
        for i in range(a3):
            if p2[i] > p3[i]:
                flag = 1

        if flag == 0:
            c += 1

    print(c)


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
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
