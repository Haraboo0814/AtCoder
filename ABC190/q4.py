import sys
from io import StringIO
import unittest


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def resolve():
    n = int(input())
    max_n = 2 * n
    ans = 0
    divisors = make_divisors(max_n)
    for d in divisors:
        if (max_n / d - (d - 1)) % 2 == 0:
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
        input = """12"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """963761198400"""
        output = """1920"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
