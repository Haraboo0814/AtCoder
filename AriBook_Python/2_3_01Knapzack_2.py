n = 4
# (w, v)
goods = [(2, 3), (1, 2), (3, 4), (2, 2)]
W = 5

MAX_V = 100
MAX_N = 100
INF = 10**8

# DPテーブル
dp = [[INF for i in range(MAX_N * MAX_V + 1)] for j in range(MAX_N + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(MAX_N * MAX_V + 1):
        if j < goods[i][1]:  # (価値で制限して)i番目の品物が入れれない
            dp[i+1][j] = dp[i][j]
        else:   # i番目の品物が入れれる
            # 一つ前の状態 と i番目の品物を入れた場合を比較
            dp[i+1][j] = min(dp[i][j], dp[i][j - goods[i][1]] + goods[i][0])

ans = 0
for i in range(MAX_N * MAX_V + 1):
    if dp[n][i] <= W:   # i:要領を超えていない価値のインデックス
        ans = i
print(ans)
