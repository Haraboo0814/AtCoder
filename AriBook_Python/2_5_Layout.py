INF = 10**18
N = 4
ML = 2
MD = 1
AL = [1, 2]
BL = [3, 4]
DL = [10, 20]
AD = [2]
BD = [3]
DD = [3]

d = [INF for i in range(N)]
d[0] = 0

# ベルマンフォード法
for k in range(N):
    # i + 1 から i へコスト 0
    for i in range(N - 1):
        if d[i + 1] < INF:
            d[i] = min(d[i], d[i + 1])
    # AL から BL へコスト DL
    for i in range(ML):
        if d[AL[i] - 1] < INF:
            d[BL[i] - 1] = min(d[BL[i] - 1], d[AL[i] - 1] + DL[i])
    # BD から AD へコスト -DD
    for i in range(MD):
        if d[BD[i] - 1] < INF:
            d[AD[i] - 1] = min(d[AD[i] - 1], d[BD[i] - 1] - DD[i])

res = d[N - 1]
if d[0] < 0:
    # 負の閉路が存在 = 解なし
    res = -1
elif res == INF:
    res = -2

print(res)
