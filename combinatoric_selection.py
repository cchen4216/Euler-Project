
from math import factorial

count = 0
for n in range(2,101):
    for r in range(1,n):
        temp = factorial(n)/(factorial(r)*factorial(n-r))
        if temp > 1000000:
            count += 1
print count 
