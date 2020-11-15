import sys
from io import StringIO
import unittest

'''
いもす法
https://imoz.jp/algorithms/imos_method.html
'''


def resolve():
    import numpy as np
    n, w = map(int, input().split())
    arr = np.zeros(2*10**5 + 1)
    for i in range(n):
        s, t, p = map(int, input().split())
        arr[s] += p
        arr[t] -= p

    cmsm = np.cumsum(arr)
    if cmsm.max() > w:
        print("No")
    else:
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
        input = """4 10
1 3 5
2 4 4
3 10 6
2 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 10
1 3 5
2 4 4
3 10 6
2 3 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 1000000000
0 200000 999999999
2 20 1
20 200 1
200 2000 1
2000 20000 1
20000 200000 1"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
