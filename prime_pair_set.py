
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

def check_pair(num1, num2):
    if not isprime(cat(num1, num2)):
        return False
    if not isprime(cat(num2, num1)):
        return False
    return True


primes = [3]
for i in range(7,10000,2):
    if isprime(i):
        primes.append(i)
print len(primes)
#print primes.index(3), primes.index(7), primes.index(109), primes.index(673)
#quit()

primeDict = dict.fromkeys(primes)
primeDict[3] = []

for i in range(1,len(primes)):
    primeDict[primes[i]] = []
    for j in range(i):
        if check_pair(primes[i], primes[j]):
            primeDict[primes[j]].append(primes[i])
            primeDict[primes[i]].append(primes[j])

#for i,j in primeDict.items():
#    print i, j

testcount = 0
for i in primeDict.keys():
    for j in primeDict[i]:
        if i > j: continue
        temp = set(primeDict[i]).intersection(set(primeDict[j]))
        temp = sorted(list(temp))
        if len(temp) >= 3 :
            #print i, j, temp
            for k in range(len(temp)-2):
                for m in range(k+1,len(temp)-1):
                    for n in range(m+1, len(temp)):
                        #if testcount> 4: quit()
                        #testcount += 1
                        list1 = primeDict[temp[k]] + [temp[k]]
                        list2 = primeDict[temp[m]] + [temp[m]]
                        list3 = primeDict[temp[n]] + [temp[n]]
                        temp2 = set(list1).intersection(set(list2))
                        temp2 = temp2.intersection(set(list3))
                        temp2 = temp2.intersection(set(temp))
                        temp2 = list(temp2)
                        if len(temp2)>=3:
                            print i, j, temp[k], temp[m], temp[n], temp2
