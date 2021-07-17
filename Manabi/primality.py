def is_prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return n != 1


def divisor(n):
    res = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            res.append(i)
            if n != n / i:
                res.append(n / i)

        i += 1


def prime_factor(n):
    res = []
    i = 2
    while i**2 <= n:
        while n % i == 0:
            res[i] += 1
            n //= i

        i += 1
    if n != 1:
        res[n] = 1
    return res
