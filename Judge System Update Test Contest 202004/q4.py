import sys
from io import StringIO
import unittest


def resolve():
    from math import gcd

    def binarySearch(x):
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if gcd(x, a[mid]) == 1:
                right = mid
            else:
                left = mid + 1
        return gcd(x, a[-1]) if right == n else left + 1

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(map(int, input().split()))

    for i in range(n-1):
        a[i+1] = gcd(a[i], a[i+1])

    for i in range(q):
        print(binarySearch(s[i]))


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
        input = """4 3\n6 12 6 9\n4 6 3"""
        output = """4\n3\n3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3\n4 6 2 1\n3 2 1000000000"""
        output = """1\n4\n4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
