from math import sqrt

def isprime(num):
    a = int(sqrt(num))
    if num < 2: return False
    if num == 2: return True
    if num%2==0: return False
    for i in range(3, a+1, 2):
        if num%i == 0:
            return False
    return True

def get_permutations(num):
    list1 = []
    if num<1000 or num>9999:
        print 'Error in get_permutations!'
        quit()
    d0 = num%10; num /= 10
    d1 = num%10; num /= 10
    d2 = num%10; num /= 10
    d3 = num%10

    temp = d3*1000 + d2*100 + d0*10 + d1
    if temp>=1000: list1.append(temp)
    temp = d3*1000 + d1*100 + d0*10 + d2
    if temp>=1000: list1.append(temp)
    temp = d3*1000 + d1*100 + d2*10 + d0
    if temp>=1000: list1.append(temp)
    temp = d3*1000 + d0*100 + d1*10 + d2
    if temp>=1000: list1.append(temp)
    temp = d3*1000 + d0*100 + d2*10 + d1
    if temp>=1000: list1.append(temp)

    temp = d2*1000 + d3*100 + d0*10 + d1
    if temp>=1000: list1.append(temp)
    temp = d2*1000 + d3*100 + d1*10 + d0
    if temp>=1000: list1.append(temp)
    temp = d2*1000 + d1*100 + d0*10 + d3
    if temp>=1000: list1.append(temp)
    temp = d2*1000 + d1*100 + d3*10 + d0
    if temp>=1000: list1.append(temp)
    temp = d2*1000 + d0*100 + d3*10 + d1
    if temp>=1000: list1.append(temp)
    temp = d2*1000 + d0*100 + d1*10 + d3
    if temp>=1000: list1.append(temp)

    temp = d1*1000 + d3*100 + d0*10 + d2
    if temp>=1000: list1.append(temp)
    temp = d1*1000 + d3*100 + d2*10 + d0
    if temp>=1000: list1.append(temp)
    temp = d1*1000 + d2*100 + d0*10 + d3
    if temp>=1000: list1.append(temp)
    temp = d1*1000 + d2*100 + d3*10 + d0
    if temp>=1000: list1.append(temp)
    temp = d1*1000 + d0*100 + d2*10 + d3
    if temp>=1000: list1.append(temp)
    temp = d1*1000 + d0*100 + d3*10 + d2
    if temp>=1000: list1.append(temp)

    temp = d0*1000 + d3*100 + d2*10 + d1
    if temp>=1000: list1.append(temp)
    temp = d0*1000 + d3*100 + d1*10 + d2
    if temp>=1000: list1.append(temp)
    temp = d0*1000 + d2*100 + d3*10 + d1
    if temp>=1000: list1.append(temp)
    temp = d0*1000 + d2*100 + d1*10 + d3
    if temp>=1000: list1.append(temp)
    temp = d0*1000 + d1*100 + d3*10 + d2
    if temp>=1000: list1.append(temp)
    temp = d0*1000 + d1*100 + d2*10 + d3
    if temp>=1000: list1.append(temp)

    return list(set(list1))

for i in range(1000, 10000):
    if not isprime(i): continue
    list1 = get_permutations(i)
    for k in list1:
        if k<=i: list1.remove(k)
    if len(list1)<2: continue
    #print i, len(list1), list1
    for j in list1:
        if j == i: continue
        k = 2*j - i
        if k not in list1: continue
        if not isprime(j) or not isprime(k): continue
        print i, j, k
