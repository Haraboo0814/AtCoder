import sys
from io import StringIO
import unittest

'''
ベクトル総当たりで可
'''


def resolve():
    import itertools
    from collections import defaultdict
    n = int(input())
    V = []
    for _ in range(n):
        x, y = map(int, input().split())
        V.append((x, y))

    for i in range(n):
        for j in range(i):
            for k in range(j):
                x1, y1 = V[i]
                x2, y2 = V[j]
                x3, y3 = V[k]
                x1 -= x3
                y1 -= y3
                x2 -= x3
                y2 -= y3
                if x2 * y1 == x1 * y2:
                    print("Yes")
                    return

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
        input = """4
0 1
0 2
0 3
1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14
5 5
0 1
2 5
8 0
2 1
0 0
3 6
8 6
5 9
7 9
3 4
9 2
9 8
7 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
8 2
2 3
1 3
3 7
1 0
8 8
5 6
9 7
0 1"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
