import itertools

A = []
for i in range(3):
    A_i = list(map(int, input().split()))
    A.append(A_i)

A = list(itertools.chain.from_iterable(A))
N = int(input())

for _ in range(N):
    b = int(input())
    for i, a in enumerate(A):
        if a == b:
            A[i] = 0
            break
    if A[0] == A[1] == A[2] or A[3] == A[4] == A[5] or A[6] == A[7] == A[8] or A[0] == A[3] == A[6] or A[1] == A[4] == A[7] or A[2] == A[5] == A[8] or A[0] == A[4] == A[8] or A[2] == A[4] == A[6]:
        print('Yes')
        exit()

print('No')
