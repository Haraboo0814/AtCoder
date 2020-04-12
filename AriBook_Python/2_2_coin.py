V = [1, 5, 10, 50, 100, 500]
C = [3, 2, 1, 3, 0, 2]
a = 620
ans = 0

for i in range(5, -1, -1):
    t = min(a // V[i], C[i])
    a -= t * V[i]
    ans += t

print(ans)
