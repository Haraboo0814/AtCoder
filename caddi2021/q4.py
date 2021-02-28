import sys
from io import StringIO
import unittest
import collections


def resolve():
    k = int(input())
    s = input()
    t = input()
    ans = 0
    n = 0
    for i in range(1, 10):
        for j in range(1, 10):
            limit_i = k - s.count(str(i)) - t.count(str(i))
            limit_j = k - s.count(str(j)) - t.count(str(j))
            if i == j:
                limit_j -= 1
            s_temp = list(s + str(i))
            t_temp = list(t + str(j))
            if limit_i > 0 and limit_j > 0:
                n += limit_i * limit_j
                s_cnt = collections.Counter(s_temp)
                t_cnt = collections.Counter(t_temp)

                s_score = 0
                t_score = 0
                for l in range(1, 10):
                    s_score += l * 10 ** s_cnt[str(l)]
                    t_score += l * 10 ** t_cnt[str(l)]

                if s_score > t_score:
                    ans += limit_i * limit_j

    print(ans / n)


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
        input = """2
1144#
2233#"""
        output = """0.4444444444444444"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
9988#
1122#"""
        output = """1.0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1122#
2228#"""
        output = """0.001932367149758454"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000
3226#
3597#"""
        output = """0.6296297942426154"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
