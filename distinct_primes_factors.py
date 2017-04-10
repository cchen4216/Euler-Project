
from math import sqrt
maxnum = 10000

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
    for i in range(3,num,2):
        if isprime(i):
            list1.append(i)
    return list1

primes = get_primes(maxnum)

def decompose(num):
    global primes
    list1 = []
    for i in primes:
        factor = 1
        while True:
            if num%i == 0:
                factor *= i
                num /= i
                continue
            else:
                break
        if factor != 1: list1.append(factor)
        if i>num: break
    if num != 1:
        print 'Cannot find the right prime factors!!!'
    return list1
#print decompose(646)
#quit()


num = 2
while num < maxnum*maxnum :
    if isprime(num+3): num += 4; continue
    if isprime(num+2): num += 3; continue
    if isprime(num+1): num += 2; continue
    if isprime(num):   num += 1; continue
    list1 = decompose(num)
    list2 = decompose(num+1)
    list3 = decompose(num+2)
    list4 = decompose(num+3)
    if len(list4)!=4: num += 4; continue
    if len(list3)!=4: num += 3; continue
    if len(list2)!=4: num += 2; continue
    if len(list1)!=4: num += 1; continue

    set_ = set(list1 + list2 + list3 + list4)
    if len(set_)==16:
        print num
        quit()
    num += 1
