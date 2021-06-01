import sys
from io import StringIO
import unittest


"""
「 N×N のマス目に含まれる K×K の区画であって、
その区画の中に X より大きいマスが ⌊K^2/2⌋+1 個未満
であるようなものは存在するか？」
pypy3
"""


def resolve():
    n, k = map(int, input().split())
    lim = k**2 // 2 + 1
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    # S_i,j : (1,1)~(i,j) 間の X より大きいマスの数
    S = [[0 for i in range(n + 1)] for j in range(n + 1)]

    ng = -1
    ok = 10**9 + 7

    while (ng + 1) < ok:
        mid = (ok + ng) // 2

        for i in range(n):
            for j in range(n):
                S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j]
                if A[i][j] > mid:
                    S[i + 1][j + 1] += 1

        ext = False
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                # 2d 累積和
                if S[i + k][j + k] - S[i][j + k] - S[i + k][j] + S[i][j] < lim:
                    ext = True

        if ext:
            ok = mid
        else:
            ng = mid

    print(ok)


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
        input = """3 2
1 7 0
5 8 11
10 4 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1 2 3
4 5 6
7 8 9"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
