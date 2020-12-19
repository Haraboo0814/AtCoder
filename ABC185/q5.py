import sys
from io import StringIO
import unittest


class Levenshtein:
    def initArray(self, str1, str2):
        distance = []
        for i in range(len(str1)+1):
            distance.append([0]*(len(str2)+1))
            distance[i][0] = i
        for j in range(len(str2)+1):
            distance[0][j] = j
        return distance

    def editDist(self, str1, str2, distance):
        dist = [0]*3
        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                dist[0] = distance[i-1][j-1] if str1[i -
                                                     1] == str2[j-1] else distance[i-1][j-1]+1
                dist[1] = distance[i][j-1]+1
                dist[2] = distance[i-1][j]+1
                distance[i][j] = min(dist)
        return distance[i][j]

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.distance = self.initArray(str1, str2)
        self.dist = self.editDist(str1, str2, self.distance)


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    leven = Levenshtein(A, B)
    print(leven.dist)


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
        input = """4 3
1 2 1 3
1 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 6
1 3 2 4
1 5 2 6 4 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
1 1 1 1 1
2 2 2 2 2"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
