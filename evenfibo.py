a, b = 1, 2
myList = [1,2]
while b < 4000000:
    a, b = b, a + b
    myList.append(b)
result = sum([i for i in myList if i % 2 == 0])
print(result)
