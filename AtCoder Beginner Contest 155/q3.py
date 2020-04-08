N = int(input())
D = {}
for i in range(N):
    S = input()
    if S in D:
        D[S] += 1
    else:
        D[S] = 1

D_sorted = sorted(D.items(), key=lambda x: x[0])
D_sorted = sorted(D_sorted, key=lambda x: x[1], reverse=True)

top = D_sorted[0][1]
for k in D_sorted:
    if top == k[1]:
        print(k[0])
    else:
        exit()
