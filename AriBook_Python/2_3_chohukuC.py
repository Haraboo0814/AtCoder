n = 3
m = 3
a = [1, 2, 3]
M = 10000

# DPテーブル
dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
# 一つも選ばない通り数
for i in range(n + 1):
    dp[i][0] = 1

for i in range(0, n):
    for j in range(1, m + 1):
        # インデックスが負の場合を避ける
        if j - 1 - a[i] >= 0:
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i]
                            [j] - dp[i][j - 1 - a[i]]) % M
        else:
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % M

print(dp[n][m])
