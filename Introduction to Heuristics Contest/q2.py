import sys
from io import StringIO
import unittest


def resolve():
    import numpy as np
    d = int(input())
    C = list(map(int, input().split()))
    S = []
    for _ in range(d):
        _S = list(map(int, input().split()))
        S.append(_S)
    S = np.array(S)

    T = []
    for _ in range(d):
        T.append(int(input()))

    last = [1 for i in range(26)]
    score = 0
    for i in range(d):
        # max_idx = np.argmax(S[i])
        # print(max_idx + 1)
        score += S[i][T[i]]
        last[T[i]] = i
        for j in range(26):
            score -= C[j] * (d - last[j])

        print(score)


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
        input = """5
86 90 69 51 2 96 71 47 88 34 45 46 89 34 31 38 97 84 41 80 14 4 50 83 7 82
19771 12979 18912 10432 10544 12928 13403 3047 10527 9740 8100 92 2856 14730 1396 15905 6534 4650 11469 3628 8433 2994 10899 16396 18355 11424
6674 17707 13855 16407 12232 2886 11908 1705 5000 1537 10440 10711 4917 10770 17272 15364 19277 18094 3929 3705 7169 6159 18683 15410 9092 4570
6878 4239 19925 1799 375 9563 3445 5658 19857 11401 6997 6498 19933 3848 2426 2146 19745 16880 17773 18359 3921 14172 16730 11157 5439 256
8633 15862 15303 10749 18499 7792 10317 5901 9395 11433 3514 3959 5202 19850 19469 9790 5653 784 18500 10552 17975 16615 7852 197 8471 7452
19855 17918 7990 10572 4333 438 9140 9104 12622 4985 12319 4028 19922 12132 16259 17476 2976 547 19195 19830 16285 4806 4471 9457 2864 2192
1
17
13
14
13"""
        output = """18398
35037
51140
65837
79325"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()