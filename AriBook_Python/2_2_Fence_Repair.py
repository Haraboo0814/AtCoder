n = 3
L = [8, 5, 8]

cost = 0
while(n > 1):
    mii1 = 0
    mii2 = 1
    if L[mii1] > L[mii2]:
        mii1, mii2 = mii2, mii1
    # 小さい２つを探索
    for i in range(2, n):
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
        elif L[i] < L[mii2]:
            mii2 = i

    # マージ
    l = L[mii1] + L[mii2]
    cost += l
    # L[n-1] は捨てていく
    if mii1 == n - 1:
        mii1, mii2 = mii2, mii1
    L[mii1] = l
    L[mii2] = L[n-1]
    n -= 1

print(cost)
