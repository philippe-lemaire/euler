#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

# a² + b² = c²
# a + b + c = 1000
res = 1

for a in range(2,500):
    for b in range(a+1, 1000-a):
        c = 1000 - a - b
        print(a, b, c)
        if a**2 + b**2 == c**2:
            res *= a*b*c

print(res)
