import sys
from io import StringIO
import unittest


"""
単調増加 → にぶたん
"""


def resolve():
    X = input()
    m = int(input())
    for i in range(9, -1, -1):
        if str(i) in X:
            n = i
            break

    ok = 1
    ng = 10**18
    while abs(ok - ng) > 1:
        x = (ok + ng) // 2
        if(check(X, x, m)):
            ok = x
        else:
            ng = x

    print(max(0, ok - n))


def check(X, x, m):
    ret = 0
    xx = 1
    for i in range(len(X)):
        ret += int(X[len(X) - i - 1]) * xx
        if ret > m:
            return False

        xx *= x

    return ret <= m


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
        input = """22
10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999
1500"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000000000000000000000000000000000000000000000000000000
1000000000000000000"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
