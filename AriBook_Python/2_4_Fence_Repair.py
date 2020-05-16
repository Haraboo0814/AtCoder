import heapq

n = 3
L = [8, 5, 8]

que = []
ans = 0
heapq.heapify(que)
for l in L:
    heapq.heappush(que, l)

while len(que) > 1:
    l1 = heapq.heappop(que)
    l2 = heapq.heappop(que)
    ans += l1 + l2
    heapq.heappush(que, ans)

print(ans)
