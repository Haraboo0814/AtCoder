prime = [0] * 10**6
is_prime = [True] * (10**6 + 1)


def sieve(n):
    p = 0
    is_prime[0], is_prime[1] = False, False
    for i in range(2, n + 1):
        if is_prime[i]:
            prime[p] = i
            p += 1
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return p


print(sieve(1000000))
