import sys
from io import StringIO
import unittest


def resolve():
    O = list(input())
    E = list(input())
    S = ""
    while len(O) > 0 or len(E) > 0:
        if len(O) > 0:
            S += O.pop(0)
        if len(E) > 0:
            S += E.pop(0)

    print(S)


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
        input = """xyz
abc"""
        output = """xaybzc"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoderbeginnercontest
atcoderregularcontest"""
        output = """aattccooddeerrbreeggiunlnaerrccoonntteesstt"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
