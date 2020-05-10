import heapq

n = 4
l = 25
p = 10
A = [10, 14, 20, 21]
B = [10, 5, 2, 4]

A.append(l)
B.append(0)
n += 1
que = []
heapq.heapify(que)
ans = 0
pos = 0
tank = p

for i in range(n):
    d = A[i] - pos
    while(tank - d < 0):
        # 到達不可
        if len(que) == 0:
            print(-1)
            exit()

        # 以前通ったGSで補給したことにする
        tank += -que[0]
        heapq.heappop(que)
        ans += 1

    tank -= d
    pos = A[i]
    # 負にしてpush
    heapq.heappush(que, -B[i])
    print(que)

print(ans)
