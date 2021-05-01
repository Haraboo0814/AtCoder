import sys
from io import StringIO
import unittest
from collections import deque


def resolve():
    s = list(input())
    t = deque()
    rev = False
    for c in s:
        if c == "R":
            rev = not rev
        else:
            if rev:
                if len(t) > 0 and t[0] == c:
                    t.popleft()
                else:
                    t.appendleft(c)
            else:
                if len(t) > 0 and t[-1] == c:
                    t.pop()
                else:
                    t.append(c)

    if rev:
        t.reverse()

    print("".join(t))


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
        input = """ozRnonnoe"""
        output = """zone"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hellospaceRhellospace"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
