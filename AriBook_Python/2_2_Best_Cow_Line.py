n = 6
s = "ACDBCB"

a = 0
b = n - 1

ans = ""

while a < b:
    if s[a] < s[b]:
        ans += s[a]
        a += 1
    else:
        ans += s[b]
        b -= 1

ans += s[a]
print(ans)
