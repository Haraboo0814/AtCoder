n = 3
# (w, v)
goods = [(3, 4), (4, 5), (2, 3)]
W = 7

# DPテーブル
dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

for i in range(n):
    for j in range(W + 1):
        if j < goods[i][0]:  # i番目の品物が入れれない
            dp[i+1][j] = dp[i][j]
        else:   # i番目の品物が入れれる
            # 一つ前の状態 と i番目の品物を入れた場合を比較
            dp[i+1][j] = max(dp[i][j],
                             dp[i + 1][j - goods[i][0]] + goods[i][1])

print(dp[-1][-1])
