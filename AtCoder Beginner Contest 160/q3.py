import sys
from io import StringIO
import unittest


def resolve():
    k, n = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(k + A[0])
    B = [A[i + 1] - A[i] for i in range(len(A) - 1)]

    print(k - max(B))


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
        input = """20 3\n5 10 15"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 3\n0 5 15"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
