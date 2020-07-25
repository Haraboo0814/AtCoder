import sys
from io import StringIO
import unittest


def resolve():
    def popcnt(x):
        return bin(x).count("1")

    N = int(input())
    Xs = input()
    X = int(Xs, 2)
    d = popcnt(X)

    lut = [0] * N
    for i in range(1, N):
        Xi = i % popcnt(i)
        lut[i] = lut[Xi] + 1

    dp = d+1
    dm = d-1
    mp = X % dp
    mm = X % dm if dm else 0
    # print(lut)
    # print(format(X, 'b'))

    ans = []
    for i in range(N):
        mask = 1 << (N-i-1)
        Xi = X ^ mask
        _ans = 0
        if Xs[i] == '1':
            if dm:
                m = (mm - pow(2, N-i-1, dm)) % dm
                _ans = lut[m] + 1
            # m = (mm - mask) % dm
        else:
            # m = (mp + mask) % dp
            m = (mp + pow(2, N-i-1, dp)) % dp
            _ans = lut[m] + 1
        ans.append(_ans)
    print(*ans, sep='\n')


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
011"""
        output = """2
1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """23
00110111001011011001110"""
        output = """2
1
2
2
1
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
2
1
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
