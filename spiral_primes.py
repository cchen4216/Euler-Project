
import numpy as np
from math import sqrt

def isprime(n):
    a = int(sqrt(n))
    if n<2: return False
    if n==2: return True
    for i in range(3, a+1, 2):
        if n%i==0:
            return False
    return True

def calc_prime_ratio(M):
    length = len(M)
    count = 0
    for i in range(length):
        if isprime(M[i][i]):
            count += 1
        if isprime(M[i][length-i-1]):
            count += 1
    return float(count)/float(2*length-1)

Matrix = [[1]]
count = 2
countprime = 0

for sidelength in range(3,100000,2):
    # generate new layer
    #for i in range(len(Matrix)-1, -1, -1):
    for i in range(sidelength-2-1, -1, -1):
        #Matrix[i].insert(len(Matrix[i]), count)
        count += 1
    if isprime(count):
        countprime += 1

    #Matrix.insert(0, range(count+sidelength-1, count-1, -1))
    count += sidelength
    if isprime(count-1):
        countprime += 1

    #for i in range(1, len(Matrix)):
    for i in range(1, sidelength-1):
        #Matrix[i].insert(0, count)
        count += 1
    if isprime(count):
        countprime += 1

    #Matrix.insert(len(Matrix), range(count, count+sidelength))
    count += sidelength
    if isprime(count-1):
        countprime += 1
    #print sidelength

    # check percentage of primes
    #if isprime(Matrix[0][0]):
    #    countprime += 1
    #if isprime(Matrix[sidelength-1][sidelength-1]):
    #    countprime += 1
    #if isprime(Matrix[0][sidelength-1]):
    #    countprime += 1
    #if isprime(Matrix[sidelength-1][0]):
    #    countprime += 1
    temp = float(countprime)/(2*sidelength-1)
    print sidelength, countprime, temp
    if temp < 0.1:
        quit()

    #if sidelength > 10000:
    #    temp = calc_prime_ratio(Matrix)
    #    print sidelength, temp
    #    if temp < 0.1: quit()


#print np.array(Matrix)
