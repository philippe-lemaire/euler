'''
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def fac(n):
    return 1 if (n < 1) else n * fac(n-1)

res = 0

def is_sum_of_factorials_of_digits_equal_to_number(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    
    my_sum = 0
    for digit in digits:
        my_sum += fac(digit)
        
    return my_sum == n

#TEST

#print (is_sum_of_factorials_of_digits_equal_to_number(145))
#print (is_sum_of_factorials_of_digits_equal_to_number(146))

selected_numbers = []

for candidate in range (3, 10000000):
    if is_sum_of_factorials_of_digits_equal_to_number(candidate):
        selected_numbers.append(candidate)
    
print (selected_numbers)
print(sum(selected_numbers))


