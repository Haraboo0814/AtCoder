# ≒ ax + by = 1となる整数x,yを求める

def extgcd(a, b):
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y


d, x, y = extgcd(4, 11)
if d == 1:
    L = [0] * 4
    if x > 0:
        L[0] += x
    else:
        L[1] -= x
    if y > 0:
        L[2] += y
    else:
        L[3] -= y
    print(*L)
else:
    print(-1)
