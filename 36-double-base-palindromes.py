'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

double_based_palindromes = []


def is_palindrome_base10(n):
    my_string = str(n)
    return my_string == my_string[::-1]

def is_palindrome_base2(n):
    my_bin_string = bin(n)[2:]
    return my_bin_string == my_bin_string[::-1]



for candidate in range(0,1000001):
    if is_palindrome_base10(candidate) and is_palindrome_base2(candidate):
        double_based_palindromes.append(candidate)
        print(candidate, " added to the list of double based palindromes")
        
print("The sum of double based palindromes under 1 million is ", sum(double_based_palindromes))
