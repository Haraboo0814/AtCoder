import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    bk = [[] for i in range(200)]

    cnt = min(n, 8)
    for i in range(1, 1 << cnt):
        sig = 0
        s = []
        for j in range(cnt):
            if i & (1 << j):
                s.append(j + 1)
                sig += A[j]
                sig %= 200

        if(len(bk[sig]) != 0):
            print("Yes")
            print(len(bk[sig]), *bk[sig])
            print(len(s), *s)
            return

        else:
            bk[sig] = s

    print("No")


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
        input = """5
180 186 189 191 218"""
        output = """Yes
1 1
2 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
123 523"""
        output = """Yes
1 1
1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
2013 1012 2765 2021 508 6971"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
