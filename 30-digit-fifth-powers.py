'''
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴
8208 = 8⁴ + 2⁴ + 0⁴ + 8⁴
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
As 1 = 1⁴ is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def sum_of_fifths(n):
    stringn = str(n)
    res = 0
    for digit in stringn:
        res += int(digit)**5
    return res

mylist = []

for n in range(2, 1000000):
    if n == sum_of_fifths(n):
        mylist.append(n)

print(mylist)
print(sum(mylist))
