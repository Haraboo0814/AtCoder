# 選べる仕事の中で、終了時間が早いものを選ぶことを繰り返す．

n = 5
S = [1, 2, 4, 6, 8]
T = [3, 5, 7, 9, 10]
itv = zip(T, S)

itv = sorted(itv)
T, S = zip(*itv)

ans = 0
t = 0
for i in range(n):
    # 重ならない仕事
    if t < S[i]:
        ans += 1
        t = T[i]

print(ans)
