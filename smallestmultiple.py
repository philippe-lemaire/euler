def isEvenlyDivisible(n, m):
# tests if n is evenly divisible by numbers from 1 to m.
    for i in reversed(range(2, m+1)):
        if n % i != 0:
            return False
    return True


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

factors = [i for i in range(1, 21) if is_a_prime(i)]
res = 1
for factor in factors:
    res *= factor


j = 0
counter = 0
while True:
    j += res
    counter += 1
    if isEvenlyDivisible(j,20):
        print(j)
        print(counter)
        break
    else:
        print(j, "NOK")
