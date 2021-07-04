import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())
    A, B, C, D = [], [], [], []
    x1, x2, y1, y2 = 0, 0, 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        # 重心を計算
        x1 += a
        y1 += b
        # スケール調整
        A.append(a * n)
        B.append(b * n)
    for i in range(n):
        c, d = map(int, input().split())
        x2 += c
        y2 += d
        C.append(c * n)
        D.append(d * n)

    for i in range(n):
        # 重心を原点に
        A[i] -= x1
        B[i] -= y1
        C[i] -= x2
        D[i] -= y2

    for i in range(n):
        if A[i] != 0 or B[i] != 0:
            A[i], A[0] = A[0], A[i]
            B[i], B[0] = B[0], B[i]

    eps = 1e-6
    ans = "No"
    for i in range(n):
        angle = math.atan2(D[i], C[i]) - math.atan2(B[0], A[0])
        flag = True
        for j in range(n):
            # A, BをC, Dに合わせて回転
            a = A[j] * math.cos(angle) - B[j] * math.sin(angle)
            b = A[j] * math.sin(angle) + B[j] * math.cos(angle)
            flag2 = False
            for k in range(n):
                if abs(a - C[k]) <= eps and abs(b - D[k]) <= eps:
                    flag2 = True

            flag &= flag2

        if flag:
            ans = "Yes"

    print(ans)


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
        input = """3
0 0
0 1
1 0
2 0
3 0
3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 0
1 1
3 0
-1 0
-1 1
-3 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0
2 9
10 -2
-6 -7
0 0
2 9
10 -2
-6 -7"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6
10 5
-9 3
1 -5
-6 -5
6 9
-9 0
-7 -10
-10 -5
5 4
9 0
0 -10
-10 -2"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
