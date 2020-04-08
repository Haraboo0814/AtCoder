import sys
from io import StringIO
import unittest


def resolve():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_a = min(a)
    min_b = min(b)
    ans = min_a + min_b
    for _ in range(M):
        i, j, c = map(int, input().split())
        ans = min(ans, a[i - 1] + b[j - 1] - c)

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
        input = """2 3 1\n3 3\n3 3 3\n1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 2\n10\n10\n1 1 5\n1 1 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1\n3 5\n3 5\n2 2 2"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
