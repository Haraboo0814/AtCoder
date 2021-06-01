import sys
from io import StringIO
import unittest


def resolve():
    A = list(map(int, input().split()))
    B = [0] * 6
    for a in A:
        B[a - 1] += 1
    ans = 0
    for i, b in enumerate(B):
        if b == 3:
            print(i + 1)
            return
        if b == 1 and ans == 0:
            ans = i + 1
        elif b == 1 and ans != 0:
            print(0)
            return
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
        input = """2 5 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
