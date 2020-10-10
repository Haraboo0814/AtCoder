import sys
from io import StringIO
import unittest


'''
iが大きくなるにつれ追加された整数の種類数が徐々に増えていくことを考えると、 
iが大きくなるにつれ答えも増加すること(減少しないこと)が考えられます。
よって、あるiに対する答えを求めたいときは、i−1について求めた答え以上の値で、
今まで追加した整数の中に登場しない最小の値を求めれば良いです。
これは値を小さい順に一つずつ試していき(※)、見つけたところで
ループを抜けるという実装でも合計でO(N)回の(※)で済みます。
'''


def resolve():
    n = int(input())
    cand = [0 for i in range(200005)]
    P = list(map(int, input().split()))
    at = 0
    for p in P:
        cand[p] += 1
        while cand[at]:
            at += 1
        print(at)


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
        input = """4
1 1 0 2"""
        output = """0
0
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
5 4 3 2 1 0 7 7 6 6"""
        output = """0
0
0
0
0
6
6
6
8
8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
