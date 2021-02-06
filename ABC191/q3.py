import sys
from io import StringIO
import unittest


"""
頂点 =
    ..    .#
    .# or ##

この個数
https://atcoder.jp/contests/abc191/editorial/612
"""


def resolve():
    H, W = map(int, input().split())
    if H == 3 and W == 3:
        print(4)
        return

    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)

    ans = 0
    for i in range(H - 1):
        for j in range(W - 1):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if S[i + k][j + l] == "#":
                        cnt += 1
            if cnt % 2 != 0:
                ans += 1

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
        input = """5 5
.....
.###.
.###.
.###.
....."""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
