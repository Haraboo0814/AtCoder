n = 6
r = 10
X = [1, 7, 15, 20, 30, 50]

i = 0
ans = 0
while i < n:
    s = X[i]    # 左側
    i += 1
    # +rまで行けるとこまで
    while(i < n and X[i] <= s + r):
        i += 1
    p = X[i-1]  # 印
    # +rまで行けるとこまで
    while(i < n and X[i] <= p + r):
        i += 1
    ans += 1

print(ans)
