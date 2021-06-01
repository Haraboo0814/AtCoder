import sys
from io import StringIO
import unittest
from collections import defaultdict


def resolve():
    n, k = map(int, input().split())
    idx = 0
    d = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        d[a] += b
    d = sorted(d.items(), key=lambda k_v: k_v[0], reverse=False)
    for a, b in d:
        if k >= a - idx:
            k += b
            k -= a - idx
            idx = a
        else:
            idx += k
            k = 0
            break

    print(idx + k)


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
        input = """2 3
2 1
5 10"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1000000000
1 1000000000
2 1000000000
3 1000000000
4 1000000000
5 1000000000"""
        output = """6000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
5 5
2 1
2 2"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
