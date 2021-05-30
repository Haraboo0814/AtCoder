import sys
from io import StringIO
import unittest

"""
a** or b** の数をnCkで出し、
頭から決める
"""


def resolve():
    a, b, k = map(int, input().split())
    ans = ""
    # nCkの値
    c = [[0 for i in range(61)] for j in range(61)]
    c[0][0] = 1
    for i in range(60):
        for j in range(i + 1):
            c[i + 1][j] += c[i][j]
            c[i + 1][j + 1] += c[i][j]

    while a + b > 0:
        x = 0
        if a >= 1:
            x = c[a + b - 1][a - 1]
        if k <= x:
            ans += "a"
            a -= 1
        else:
            ans += "b"
            b -= 1
            k -= x

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
        input = """2 2 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 30 118264581564861424"""
        output = """bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
