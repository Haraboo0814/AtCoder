import bisect

INF = 10**8
n = 5
a = [4, 2, 3, 1, 5]

# DPテーブル
dp = [INF for i in range(n)]
ans = 0

for i in range(n):
    dp[bisect.bisect_left(dp, a[i])] = a[i]
    print(dp)
print(bisect.bisect_left(dp, INF))
