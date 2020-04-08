import sys
from io import StringIO
import unittest


def resolve():
    import copy

    h, w = map(int, input().split())
    board = []
    for i in range(h):
        board.append(list(input()))

    temp_board = copy.deepcopy(board)

    def reset():
        board = copy.deepcopy(temp_board)

    x, y = 0, 0
    ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(x, y, m):
        if x == w - 1 and y == h - 1:
            return m
        ans = []
        for (dx, dy) in ds:
            if -1 < x + dx < w and -1 < y + dy < h:
                if board[y + dy][x + dx] == ".":
                    m = dfs(x + dx, y + dy, m)
                else:
                    # board[y + dy][x + dx] = "."
                    # for b in board:
                    #   print(b)
                    m = dfs(x + dx, y + dy, m + 1)
            ans.append(m)
        # reset()
        print(ans)
        return min(ans)

    print(dfs(0, 0, 0))


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
        input = """3 3\n.##\n.#.\n##."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2\n#.\n.#"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4\n..##\n#...\n###.\n###."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 5\n.#.#.\n#.#.#\n.#.#.\n#.#.#\n.#.#."""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
