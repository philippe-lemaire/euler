'''
Quadratic primes
Problem 27
Published on Friday, 27th September 2002, 06:00 pm; Solved by 55166; Difficulty rating: 5%
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

def is_a_prime(n):
    ''' takes a positive integer as argument. Returns True if it's a prime number, False if it's not a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max = n**0.5 + 1
    i = 3

    while i <= max:
        if n % i == 0:
            return False
        i = i + 2
    return True


def quadratic(n, a, b):
    return n**2 + a * n + b


def count_primes(a, b):
    n = 0
    while is_a_prime(quadratic(n, a, b)):
        n += 1
    return n


mylist = []
best = 0
best_coefs = (0,0)
for a in range(-999, 1000):
    for b in range(-999, 1000):
        challenger = count_primes(a, b)
        if  challenger > best:
            best = challenger
            best_coefs = (a , b)

print("n² +" , best_coefs[0],"n +" , best_coefs[1],"donne", best, "nombres premiers consécutifs")
print("le dernier mot = ", best_coefs[0] * best_coefs[1])

