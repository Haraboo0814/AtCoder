N, M = map(int, input().split())
S = []
C = []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s - 1)
    C.append(c)

num = ['*'] * N

for s, c in zip(S, C):
    if s == 0 and c == 0 and N != 1:
        print(-1)
        exit()
    if num[s] == '*':
        num[s] = str(c)
    elif num[s] != str(c):
        print(-1)
        exit()

if num[0] == '*' and N != 1:
    num[0] = '1'
print(''.join(num).replace('*', '0'))
