from math import sqrt

def isprime(num):
    a = int(sqrt(num))
    if num<2: return False
    if num==2: return True
    if num%2==0: return False
    for i in range(3, a+1, 2):
        if num%i==0:
            return False
    return True

def get_primes(num):
    list1 = [2]
    if num<2:
        print 'Error(get_primes): num must >= 2'
        quit()
    for i in range(3, num, 2):
        if isprime(i):
            list1.append(i)
    return list1

#print get_primes(20)

primes = get_primes(1000000)
maxprime = max(primes)
length = len(primes)
maxlen = 0
for i in range(length-1):
    for j in range(i+1, length):
        summ = sum(primes[i:j+1])
        if summ in primes and maxlen < j+1-i:
            maxlen = j+1-i
            print summ, maxlen, primes[i]
