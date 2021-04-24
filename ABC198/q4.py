import sys
from io import StringIO
import unittest
import itertools

# pypy3

def resolve():
    s1 = input()
    s2 = input()
    s3 = input()
    s = set(s1 + s2 + s3)
    # 11種以上の文字はfalse
    if len(s) > 10:
        print('UNSOLVABLE')
        return

    # 最上位はnonzero
    non_zero = set(s1[0] + s2[0] + s3[0])

    for digits in itertools.permutations(range(10), len(s)):
        dic = {c: digits[i] for i, c in enumerate(s)}
        # 最上位はnonzero
        if any(dic[c] == 0 for c in non_zero):
            continue
        if (dic[s1[-1]] + dic[s2[-1]]) % 10 != dic[s3[-1]]:
            continue
        n1 = ''.join((str(dic[c]) for c in s1))
        n2 = ''.join((str(dic[c]) for c in s2))
        n3 = ''.join((str(dic[c]) for c in s3))
        if int(n1) + int(n2) == int(n3):
            print(n1)
            print(n2)
            print(n3)
            return
    print('UNSOLVABLE')


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
        input = """a
b
c"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """x
x
y"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """p
q
p"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """abcd
efgh
ijkl"""
        output = """UNSOLVABLE"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """send
more
money"""
        output = """9567
1085
10652"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
