import sys
from io import StringIO
import unittest


def resolve():
    s = list(input())
    cnt = 0
    m_cnt = 0
    for c in s:
        if c == 'R':
            cnt += 1
            if cnt > m_cnt:
                m_cnt = cnt

        else:
            cnt = 0

    print(m_cnt)


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
        input = """RRS"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """SSS"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """RSR"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
