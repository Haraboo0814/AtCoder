l = 10
n = 3
x = [2, 6, 7]

mi = 0
ma = 0
for a in x:
    b = l - a
    mi = max(mi, min(a, b))
    ma = max(ma, a, b)

print(mi, ma)
