import sys
from io import StringIO
import unittest


def resolve():
    H, W = map(int, input().split())
    ans = 0
    table = []
    for _ in range(H):
        table.append(list(input()))

    for h in range(H):
        for w in range(W):
            if w + 1 < W and table[h][w] == table[h][w + 1] == '.':
                ans += 1
            if h + 1 < H and table[h][w] == table[h + 1][w] == '.':
                ans += 1

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
        input = """2 3
..#
#.."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
.#
#."""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
