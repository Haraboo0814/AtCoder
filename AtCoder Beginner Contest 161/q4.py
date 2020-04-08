import sys
from io import StringIO
import unittest

'''
小さいものからk番目→キューに候補追加しつつpopleft
'''


def resolve():
    from collections import deque

    k = int(input())
    q = deque(range(1, 10))

    for i in range(k):
        x = q.popleft()
        if x % 10 != 0:
            q.append(10 * x + x % 10 - 1)
        q.append(10 * x + x % 10)
        if x % 10 != 9:
            q.append(10 * x + x % 10 + 1)

    print(x)


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
        input = """15"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13"""
        output = """21"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000"""
        output = """3234566667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
