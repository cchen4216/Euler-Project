
from math import sqrt
def isprime(n):
    a = int(sqrt(n))
    if n<2: return False
    if n==2: return True
    if n%2==0: return False
    for i in range(3,a+1,2):
        if n%i==0: return False
    return True

def cat(n1, n2):
    list1 = []
    while n2 != 0 :
        list1.append(n2%10)
        n2 /= 10
    while n1 != 0:
        list1.append(n1%10)
        n1 /= 10
    list1.reverse()
    num = 0
    for i in list1:
        num = num*10 + i
    return num
#print cat(123, 4567)
#quit()

def check_pair(pairs):
    global primes
    n = len(pairs)

    for i in range(n-1,n-2,-1):
        for j in range(n-1):
            if not isprime(cat(pairs[i], pairs[j])):
                return False
            if not isprime(cat(pairs[j], pairs[i])):
                return False
    return True
#pairs = [3,7,109, 673]
#print check_pair(pairs)
#quit()

primes = []
for i in range(3,1000000,2):
    if isprime(i):
        primes.append(i)
print len(primes)
#print primes.index(3), primes.index(7), primes.index(109), primes.index(673)
#quit()

indx = [0,2,27,120,121]
while True:
    #raw_input(indx)
    temp = [primes[indx[0]], primes[indx[1]], primes[indx[2]],
            primes[indx[3]], primes[indx[4]]]

    if check_pair(temp):
        print sum(temp), temp
        quit()

    indx[-1] += 1



#    indxmin = min(indx)
#    temp2 = indx.index(indxmin)
#    while True:
#        indxmin += 1
#        if indxmin >= len(primes):
#            print "Not such pairs found in this primes list!"
#            quit()
#        if indxmin not in indx :
#            indx[temp2] = indxmin
#            break
