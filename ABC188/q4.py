import sys
from io import StringIO
import unittest

# a(b)日に料金が上がる(下がる)イベント
# イベントを順にソートし経過日数と料金を足していく


def resolve():
    n, cost = map(int, input().split())
    event = []
    for i in range(n):
        a, b, c = map(int, input().split())
        event.append((a - 1, c))
        event.append((b, -c))

    event.sort()
    ans = 0
    fee = 0
    t = 0
    for (x, y) in event:
        if x != t:
            ans += min(cost, fee) * (x - t)
            t = x

        fee += y

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
        input = """2 6
1 2 4
2 2 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """163089627821228"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """88206004785464"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
