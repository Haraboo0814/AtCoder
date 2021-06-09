import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    D = [[] for i in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        D[a - 1].append(b - 1)

    past = [0 for i in range(n)]

    def dfs(i):
        past[i] = 1
        ans = 1
        for d in D[i]:
            if past[d] != 1:
                ans += dfs(d)
        return ans

    ans = 0
    for i in range(n):
        past = [0 for i in range(n)]
        ans += dfs(i)

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
        input = """3 3
1 2
2 3
3 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
1 2
2 3
3 4
4 1"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
