N = int(input())
A = list(map(int, input().split()))
if N == len(list(set(A))):
    print('YES')
else:
    print('NO')
