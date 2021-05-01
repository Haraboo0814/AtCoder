import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    A = [tuple(map(int, input().split())) for i in range(N)]

    def check(x):
        s = set()
        for a in A:
            # 基準以上の能力値に1 (ex. (1,1,1,1,1))
            s.add(sum(1 << i for i in range(5) if a[i] >= x))
        for x in s:
            for y in s:
                for z in s:
                    # 3人の組み合わせで全て1が立つ(31 == 0b11111)
                    if x | y | z == 31:
                        return True
        return False

    # にぶたん
    ok = 0
    ng = 10**9 + 1
    while ng - ok > 1:
        cen = (ok + ng) // 2
        if check(cen):
            ok = cen
        else:
            ng = cen
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
        input = """3
3 9 6 4 6
6 9 3 1 1
8 8 9 3 7"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
6 13 6 19 11
4 4 12 11 18
20 7 19 2 5
15 5 12 20 7
8 7 6 18 5"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
6 7 5 18 2
3 8 1 6 3
7 2 8 7 7
6 3 3 4 7
12 8 9 15 9
9 8 6 1 10
12 9 7 8 2
10 3 17 4 10
3 1 3 19 3
3 14 7 13 1"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
