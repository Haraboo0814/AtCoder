n, a, b = map(int, input().split())
k = n // (a + b)
m = n % (a + b)
print(k * a + min(a, m))
