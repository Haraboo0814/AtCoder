import sys
from io import StringIO
import unittest


def resolve():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(input()))

    B = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == "-":
                B[i][j] = -1
            else:
                B[i][j] = 1

    inf = 10**18

    opt = [[-inf] * W for _ in range(H)]
    opt[H - 1][W - 1] = 0

    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if i + 1 <= H - 1:
                opt[i][j] = max(opt[i][j], -opt[i + 1][j] + B[i + 1][j])

            if j + 1 <= W - 1:
                opt[i][j] = max(opt[i][j], -opt[i][j + 1] + B[i][j + 1])

    if opt[0][0] > 0:
        print("Takahashi")
    elif opt[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")


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
        input = """3 3
---
+-+
+--"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 4
+++-
-+-+"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
-"""
        output = """Draw"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
