'''
Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
from fractions import Fraction

from numpy import prod


my_fractions = []

for denominator in range (11,100):
    for numerator in range (10, denominator):
        strnum = str(numerator)
        strden = str(denominator)
        print(strnum, " / ", strden)
        if strden[1] == '0':
            break
        if strnum[0] in strden or strnum[1] in strden:
            if strnum[0] == strden[0]:
                newnum = int(strnum[1])
                newden = int(strden[1])
            elif strnum[0] == strden[1]:
                newnum = int(strnum[1])
                newden = int(strden[0])
            elif strnum[1] == strden[1]:
                newnum = int(strnum[0])
                newden = int(strden[0])
            elif strnum[1] == strden[0]:
                newnum = int(strnum[0])
                newden = int(strden[1])
            if newnum / newden == numerator / denominator:
                my_fractions.append(Fraction(numerator, denominator))
        
print(prod(my_fractions))
    

