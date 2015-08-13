#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# functions dealing with prime numbers

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

def sum_primes(n):
    '''returns the sum of the prime numbers below n'''
    sum = 0
    j = 1
    while j < n:
        j = j + 1
        print(j)
        if is_a_prime(j):
            sum += j
    return sum

print(sum_primes(2000000))

