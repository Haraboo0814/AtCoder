n = 4
m = 4
s = "abcd"
t = "becd"

# DPテーブル
dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[i]:
            # 共通部分列長++
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            #　以前の結果の長い方
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])
