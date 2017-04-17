
from math import sqrt

def continue_fractions(root):
    minus = 0
    denom = 1
    list1 = []

    temp = int(sqrt(root))
    if temp**2==root or (temp+1)**2==root :
        return list1

    for i in range(16000):
        temp = int((sqrt(root) + minus)/denom)
        #print temp
        list1.append(temp)
        minus = minus - temp*denom
        denom = (root - minus*minus)/denom
        minus = -minus
        #print root, minus, denom
    list1.reverse()
    return list1
#print continue_fractions(13)

def count_period(list1):
    if len(list1)<10:
        return 0
    for i in range(1, len(list1)/16 - 1):
        if list1[:i]==list1[i:2*i] and\
           list1[:2*i]==list1[2*i:4*i] and\
           list1[:4*i]==list1[4*i:8*i] and\
           list1[:8*i]==list1[8*i:16*i] :
            return i

#print count_period(continue_fractions(13))
count = 0
for n in range(1,10001):
    temp = count_period(continue_fractions(n))
    if temp > 499: print n, temp
    if  temp % 2 != 0 :
        count += 1
print count
