#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def lenCollatz(n):
    currentValue = n
    counter = 1
    while True:
        if currentValue % 2 == 0:
            currentValue /= 2
            counter += 1

        else:
            currentValue = currentValue * 3 + 1
            counter += 1

        if currentValue == 1:
            break

    return counter

myList = []

for i in range(1, 1000000):
    myList.append(lenCollatz(i))
    print(i)

print(myList.index(max(myList)))
