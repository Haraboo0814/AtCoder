n = 4
# (w, v)
goods = [(2, 3), (1, 2), (3, 4), (2, 2)]
W = 5

# DPテーブル
dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

for i in range(n):
    for j in range(W + 1):
        if j < goods[i][0]:  # i番目の品物が入れれない
            dp[i+1][j] = dp[i][j]
        else:   # i番目の品物が入れれる
            # 一つ前の状態 と i番目の品物を入れた場合を比較
            dp[i+1][j] = max(dp[i][j], dp[i][j - goods[i][0]] + goods[i][1])

print(dp[-1][-1])
