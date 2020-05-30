import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    def dfs(d, tree):
        max_nodes = 2**d
        if max_nodes < A[d]:
            return -1
        if d == n:
            if A[d] == tree[d]:
                return(sum(tree))
            else:
                return -1
        tree1 = tree.append(tree[-1] * 2)
        tree2 = tree.append(tree[-1])
        l = dfs(d + 1, tree1)
        r = dfs(d + 1, tree2)
        return max(l, r)

    print(dfs(0, [1]))


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
        input = """3
0 1 1 2"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
0 0 1 0 2"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
0 3 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10
0 0 1 1 2 3 5 8 13 21 34"""
        output = """264"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
