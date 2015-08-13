def isPalindrome(n):
    inverse = str(n)[::-1]
    if str(n) == inverse:
        return True
    else:
        return False


myList = []


for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(str(i*j)):
            myList.append(i*j)

print(max(myList))


