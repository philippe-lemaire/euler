'''
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from itertools import permutations

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

primes_bom = [1, 2, 3]

for num in range(5, 1000000, 2):
    if is_a_prime(num):
        primes_bom.append(num)

counter = 0

for prime in primes_bom:
    perms = permutations(str(prime))
    gen_counter = 0
    prime_counter = 0
    for perm in perms:
        gen_counter += 1
        if is_a_prime(int("".join(perm))):
            prime_counter += 1
    if prime_counter == gen_counter:
        counter += 1
        print(int("".join(perm)), " is a circular prime")
        
print(primes_bom)
print(counter)
