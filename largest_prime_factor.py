def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(int(d))
            n /= d
        d = d + 1
        if d**2 > n:
            if n > 1: factors.append(int(n))
            break
    return factors


t = int(input())
for _ in range(t):
    print(max(prime_factors(int(input()))))