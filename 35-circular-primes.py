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

primes_bom = []

for num in range(3, 1000000, 2):
    if is_a_prime(num):
        primes_bom.append(num)


primes_trimmed = list(primes_bom)

for prime in primes_bom:
    test = str(prime)
    if ("0" in test) or ("2" in test) or ("4" in test) or ("6" in test) or ("8" in test):
        primes_trimmed.remove(prime)
        print(prime, " removed because at least one permutation would be even.")
        
primes_trimmed.insert(0,2)

final_list = list(primes_trimmed)

for prime in primes_trimmed:
    perms = permutations(str(prime))
    for perm in perms:
        if not is_a_prime(int("".join(perm))):
            final_list.remove(prime)
            print(prime, " removed because at least one permutation isn’t prime.")
            break
        
print(final_list)
print(len(final_list))
