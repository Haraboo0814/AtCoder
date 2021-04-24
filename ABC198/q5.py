import sys
from io import StringIO
import unittest
sys.setrecursionlimit(1000000)


def resolve():
    n = int(input())
    C = list(map(int, input().split()))
    G = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    ans = []
    # 経路中の色の出現回数をカウント
    check = [0] * 100005

    def dfs(i, pre):
        color = C[i]
        # 出現していない
        if check[color] == 0:
            ans.append(i + 1)
        check[color] += 1
        for pro in G[i]:
            # 戻らない
            if pro == pre:
                continue
            dfs(pro, i)
        # 出現を戻して脱出
        check[color] -= 1

    dfs(0, -1)
    ans.sort()
    print(*ans, sep='\n')


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
        input = """6
2 7 1 8 2 8
1 2
3 6
3 2
4 3
2 5"""
        output = """1
2
3
4
6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
3 1 4 1 5 9 2 6 5 3
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10"""
        output = """1
2
3
5
6
7
8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
