'''
Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so 
be sure to only include it once in your sum.
'''
import itertools

def is_pandigital(x,y):
    my_list = []
    for digit in  str(x) + str(y) + str(x * y):
        my_list.append(digit)
    my_list.sort()
    return "".join(my_list) == "123456789"

products_list = []


for multiplicand in range(2, 2000):
    for multiplier in range(2000, 2 , -1):
        if is_pandigital(multiplicand, multiplier):
            products_list.append(multiplicand * multiplier)
            

products_list = set(products_list)

print(sum(products_list))
