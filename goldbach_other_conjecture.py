
from math import sqrt

def isprime(num):
    a = int(sqrt(num))
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,a+1,2):
        if num%i==0:
            return False
    return True

def get_primes(num):
    list1 = []
    if num<2:
        return list1

    list1.append(2)
    if num==2:
        return list1

    for i in range(3, num+1, 2):
        if isprime(i):
            list1.append(i)
    return list1
#print get_primes(100)
start = 33
maxnum = 10000
primes = get_primes(maxnum)
iterator = (i for i in range(start, maxnum, 2))
for num in iterator:
    if num in primes:
        continue
    flag = True
    for i in primes:
        if i>=num:
            break
        temp = int(sqrt((num-i)/2))
        if num == i + 2*temp**2:
            flag = False
    if flag:
        print num
        quit()
