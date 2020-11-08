import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    max_cnt = 0
    ans = -1
    for i in range(2, 1001):
        cnt = 0
        for a in A:
            if a % i == 0:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            ans = i

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
        input = """3
3 12 7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
8 9 18 90 72"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1000 1000 1000 1000 1000"""
        output = """1000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
