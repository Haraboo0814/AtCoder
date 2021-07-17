import sys
from io import StringIO
import unittest
from collections import deque


def char_to_int(c):
    if ord('A') <= ord(c) <= ord('Z'):
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26


def str_to_int(a, b, c):
    return char_to_int(a) * 52 * 52 + char_to_int(b) * 52 + char_to_int(c)


def resolve():
    N = int(input())
    M = 52**3
    edge = []
    cnt = [0] * M
    rev_graph = [[] for i in range(M)]
    for _ in range(N):
        s = input()
        edge.append((str_to_int(s[0], s[1], s[2]), str_to_int(s[-3], s[-2], s[-1])))
        cnt[edge[-1][0]] += 1
        rev_graph[edge[-1][1]].append(edge[-1][0])

    ans = [-1] * M
    que = deque()
    for i in range(M):
        if cnt[i] == 0:
            ans[i] = 0
            que.append(i)

    while len(que) > 0:
        t = que.popleft()
        for x in rev_graph[t]:
            if ans[x] == -1:
                cnt[x] -= 1
                if ans[t] == 0:
                    ans[x] = 1
                    que.append(x)
                elif cnt[x] == 0:
                    ans[x] = 0
                    que.append(x)

    for i in range(N):
        if ans[edge[i][1]] == -1:
            print("Draw")
        if ans[edge[i][1]] == 0:
            print("Takahashi")
        if ans[edge[i][1]] == 1:
            print("Aoki")


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
abcd
bcda
ada"""
        output = """Aoki
Takahashi
Draw"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
ABC"""
        output = """Draw"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
eaaaabaa
eaaaacaa
daaaaaaa
eaaaadaa
daaaafaa"""
        output = """Takahashi
Takahashi
Takahashi
Aoki
Takahashi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
