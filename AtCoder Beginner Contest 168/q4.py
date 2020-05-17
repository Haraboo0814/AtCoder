import sys
from io import StringIO
import unittest


def resolve():
    from collections import deque

    n, m = map(int, input().split())
    d = {}
    par = [[] for i in range(n)]
    que = deque()
    for i in range(m):
        a, b = map(int, input().split())
        par[a - 1].append(b)
        par[b - 1].append(a)

    que.append(1)
    while(len(que) > 0):
        label = que.popleft()
        for i in par[label - 1]:
            if i not in d.keys():
                que.append(i)
                d[i] = label

    if len(d) < n:
        print("No")
        return

    print("Yes")
    for i in range(2, n + 1):
        print(d[i])


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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
