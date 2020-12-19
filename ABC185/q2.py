import sys
from io import StringIO
import unittest


def resolve():
    n, m, t = map(int, input().split())
    n0 = n
    c = 0
    for i in range(m):
        a, b = map(int, input().split())
        n -= a - c
        c = b
        if n <= 0:
            print("No")
            return
        else:
            n = min(n0, n + b - a)
            if i == m - 1:
                n -= t - b
                if n <= 0:
                    print("No")
                    return
    
    print("Yes")

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
        input = """10 2 20
9 11
13 17"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2 20
9 11
13 16"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 3 30
5 8
15 17
24 27"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 1 30
20 29"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """20 1 30
1 10"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
