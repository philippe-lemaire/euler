mynum = 2**1000

mystring = str(mynum)

res = 0

for digit in mystring:
    res += int(digit)

print(res)
