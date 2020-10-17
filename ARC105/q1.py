import sys
from io import StringIO
import unittest


def resolve():
    C = list(map(int, input().split()))
    for i in range(len(C)):
        if sum(C) - C[i] == C[i]:
            print("Yes")
            return
    if C[0] + C[1] == C[2] + C[3] or C[0] + C[2] == C[1] + C[3] or C[0] + C[3] == C[1] + C[2]:
        print("Yes")
        return
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
        input = """1 3 2 4"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
