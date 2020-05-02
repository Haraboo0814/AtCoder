n = 3
a = [3, 5, 8]
m = [3, 2, 2]
k = 17

# DPテーブル
dp = [-1 for i in range(k + 1)]
dp[0] = 0

for i in range(n):
    for j in range(k + 1):
        # j = 0 は m_i個残して作れる
        if dp[j] >= 0:
            dp[j] = m[i]
        # j を a_iで作るには大きい or j - a[i] を一個残して作れてない
        elif j < a[i] or dp[j - a[i]] <= 0:
            dp[j] = -1
        # j - a_i を一個残して作った
        else:
            dp[j] = dp[j - a[i]] - 1
    print(dp)
print(dp[-1] >= 0)
