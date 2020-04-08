N, K = map(int, input().split())
H = sorted(list(map(int, input().split())))
if N <= K:
    print('0')
elif K == 0:
    print(sum(H))
else:
    print(sum(H[:N - K]))
