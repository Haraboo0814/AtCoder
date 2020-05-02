'''
(jをi個以下に分割) = (jをi - 1個以下に分割) + (jをi個に分割)
(jをi個に分割) = (jから1をi個ずつ割り当てて、残りのj - i個をi個以下に分割)
= (j - i個をi個以下に分割)
→ dp[i][j] = dp[i-1][j] + dp[i][j-i]
'''

n = 4
m = 3
M = 10000

# DPテーブル
dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
dp[0][0] = 1

for i in range(1, m + 1):
    for j in range(n + 1):
        if j - i >= 0:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % M
        else:
            dp[i][j] = dp[i - 1][j]

print(dp)
