import sys
from io import StringIO
import unittest


'''
下３桁全てを作れるか判定
(112などはs.countから1の数をマイナス)
'''


def resolve():
    from collections import defaultdict
    import copy
    s = input()
    if len(s) == 1 and int(s) % 8 == 0:
        print("Yes")
        return
    if len(s) == 2 and (int(s) % 8 == 0 or int(''.join(list(reversed(s)))) % 8 == 0):
        print("Yes")
        return
    d = defaultdict(int)
    for i in range(1, 10):
        d[i] = s.count(str(i))

    for i in range(112, 1000, 8):
        temp = copy.deepcopy(d)
        for c in list(str(i)):
            temp[int(c)] -= 1

        if all(list(map(lambda x: x >= 0, temp.values()))):
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
        input = """1234"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1333"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
