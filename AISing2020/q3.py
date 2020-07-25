import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    d = [0 for i in range(n)]
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                if x**2 + y**2 + z ** 2 + x*y + y*z + z*x <= n:
                    d[x**2 + y**2 + z ** 2 + x*y + y*z + z*x - 1] += 1

    for i in d:
        print(i)


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
        input = """20"""
        output = """0
0
0
0
0
1
0
0
0
0
3
0
0
0
0
0
3
3
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
