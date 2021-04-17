import sys
from io import StringIO
import unittest


def resolve():
    n, p = map(int, input().split())
    ans = (p - 1) * pow_k(p - 2, n - 1)
    ans %= ((10**9) + 7)
    print(ans)


def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        x %= ((10**9) + 7)
        n //= 2

    return K * x


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
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """45108 2571593"""
        output = """224219544"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
