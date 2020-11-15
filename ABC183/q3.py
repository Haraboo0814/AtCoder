import sys
from io import StringIO
import unittest


def resolve():
    import copy
    n, k = map(int, input().split())
    T = []
    for i in range(n):
        T_i = list(map(int, input().split()))
        T.append(T_i)

    def dfs(s, cost, n, k, past=[]):
        temp = copy.deepcopy(past)
        temp.append(s)
        if len(past) == n - 1 and cost + T[s][0] == k:
            return 1
        elif len(past) == n - 1:
            return 0
        ans = 0
        for i in range(n):
            if i not in temp:
                ans += dfs(i, cost + T[s][i], n, k, temp)

        return ans

    print(dfs(0, 0, n, k, []))


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
        input = """4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
