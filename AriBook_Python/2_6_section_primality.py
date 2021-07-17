import math


# [a, b)内の素数の数
def segment_sieve(a, b):
    prime = [0] * (b - a)
    is_prime = [True] * (b - a)
    b2 = math.ceil(math.sqrt(b) - 1)
    is_prime_small = [True] * (b2 + 1)
    i = 2
    while i**2 < b:
        if is_prime_small[i]:
            # [2, √b)
            j = 2 * i
            while j**2 < b:
                is_prime_small[j] = False
                j += i
            # [a, b)
            for j in range(max(2, (a + i - 1) // i) * i, b, i):
                is_prime[j - a] = False

        i += 1
    prime = [i + a for i in range(b - a) if is_prime[i]]
    return len(prime), prime


print(segment_sieve(22, 37))
print(segment_sieve(22801763489, 22801787297))
