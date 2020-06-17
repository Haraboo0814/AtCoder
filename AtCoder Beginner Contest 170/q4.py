import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    pre_A = -1
    dp = [True for i in range(A[-1]+1)]
    for i in range(N):
        if pre_A != A[i]:
            for j in range(2, A[-1]+1):
                x = j*A[i]
                if x <= A[-1]:
                    dp[x] = False
                else:
                    break
            pre_A = A[i]
        else:
            dp[A[i]] = False

    count = 0
    for i in range(N):
        if dp[A[i]]:
            count += 1
    print(count)


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
        input = """5
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
