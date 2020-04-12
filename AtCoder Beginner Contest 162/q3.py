import sys
from io import StringIO
import unittest


def resolve():
    import math

    k = int(input())

    ans = 0
    ans += sum(range(1, k + 1))
    for i in range(1, k + 1):
        for j in range(i + 1, k + 1):
            ans += math.gcd(i, j) * 6

    if k > 2:
        for i in range(1, k + 1):
            for j in range(i + 1, k + 1):
                for l in range(j + 1, k + 1):
                    ans += math.gcd(i, math.gcd(j, l)) * 6

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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
