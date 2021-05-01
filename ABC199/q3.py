import sys
from io import StringIO
import unittest


def resolve():
    n, s, q = int(input()), list(input()), int(input())
    s1, s2 = s[:n], s[n:]
    cnt = 0
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if cnt % 2 == 1:
                s1, s2 = s2, s1
                cnt = 0
            if a <= n and b <= n:
                s1[a - 1], s1[b - 1] = s1[b - 1], s1[a - 1]
            elif a <= n and b > n:
                s1[a - 1], s2[b - 1 - n] = s2[b - 1 - n], s1[a - 1]
            elif a > n and b > n:
                s2[a - 1 - n], s2[b - 1 - n] = s2[b - 1 - n], s2[a - 1 - n]
        else:
            cnt += 1

    if cnt % 2 == 1:
        s = "".join(s2 + s1)
    else:
        s = "".join(s1 + s2)
    print(s)


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
        input = """2
FLIP
2
2 0 0
1 1 4"""
        output = """LPFI"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4"""
        output = """ILPF"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
