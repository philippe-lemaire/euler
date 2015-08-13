myNum = 600851475143


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

listOfFactors = []

factorMax = myNum**0.5 + 1
j = 3
while j <= factorMax:
    if myNum % j ==  0:
        if is_a_prime(j):
            listOfFactors.append(j)
    j += 2



print(listOfFactors)
