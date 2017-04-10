
from math import sqrt

def istriangular(num):
    a = int(sqrt(2*num))
    if a*(a+1) == 2*num:
        return True
    else:
        return False
#print istriangular(14)

def ispentagonal(num):
    a = int(sqrt(num*2/3.0)) + 1
    if a*(3*a-1) == num*2:
        return True
    else:
        return False
#print ispentagonal(36)

for i in range(1,200000):
    numh = i * (2 * i - 1)
    if istriangular(numh) and ispentagonal(numh):
        print numh

#n(n+1)/2     ---- triangular
#n(3n-1)/2    ---- pentagonal
#n(2n-1)      ---- hexagonal
