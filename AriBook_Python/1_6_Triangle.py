n = 5
a = [2, 3, 4, 5, 10]

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            l = a[i] + a[j] + a[k]
            ma = max([a[i], a[j], a[k]])
            res = l - ma
            if res > ma:
                ans = max(ans, l)

print(ans)
