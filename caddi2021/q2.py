import sys
from io import StringIO
import unittest
import math


def resolve():
    n = int(input())
    mi = 10**18
    for i in range(n):
        a, p, x = map(int, input().split())
        if x > math.ceil(a - 0.5):
            mi = min(mi, p)

    if mi == 10**18:
        print(-1)
    else:
        print(mi)


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
        input = """3
3 9 5
4 8 5
5 7 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
5 9 5
6 8 5
7 7 5"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
158260522 877914575 602436426
24979445 861648772 623690081
433933447 476190629 262703497
211047202 971407775 628894325
731963982 822804784 450968417
430302156 982631932 161735902
880895728 923078537 707723857
189330739 910286918 802329211
404539679 303238506 317063340
492686568 773361868 125660016"""
        output = """861648772"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
