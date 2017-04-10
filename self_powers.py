
summ = 0
for i in range(1, 1001):
    summ += i**i
    summ %= 10**10

print summ 
