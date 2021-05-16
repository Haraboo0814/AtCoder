import sys
from io import StringIO
import unittest


# 全パターン列挙
def resolve():
    s = list(input())
    ans = 0
    for i in range(10000):
        flag = [False] * 10
        now = i
        for _ in range(4):
            flag[now % 10] = True
            now //= 10

        flag2 = True
        for j in range(10):
            if s[j] == "o" and not flag[j]:
                flag2 = False
            if s[j] == "x" and flag[j]:
                flag2 = False
        ans += flag2

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
        input = """ooo???xxxx"""
        output = """108"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """o?oo?oxoxo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """xxxxx?xxxo"""
        output = """15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
