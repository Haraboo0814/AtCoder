H, N = map(int, input().split())
A = sum(list(map(int, input().split())))

if H <= A:
    print('Yes')
else:
    print('No')
