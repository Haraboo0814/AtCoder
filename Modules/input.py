import sys
import numpy as np
import math

sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    s = input()
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    P, Q = [], []
    for _ in range(n):
        p, q = map(int, input().split())
        P.append(p)
        Q.append(q)
