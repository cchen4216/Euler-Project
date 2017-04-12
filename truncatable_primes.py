
from math import sqrt

def isprime(num):
    a = int(sqrt(num))

    if num == 1 or num == 0 :
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, a+1, 2):
        if num % i == 0:
            return False
    return True

#print isprime(3797)
################## Main ##################
summ = 0
for num in range(10,1000000):
    flag = True
    temp = num
    while temp != 0 :
        if not isprime(temp):
            flag = False
            break
        temp /= 10
    if not flag:
        continue
    #print num

    temp1 = num
    temp2 = 0
    power = 0
    while temp1 != 0:
        temp2 = temp2 + (temp1%10) * 10**power
        temp1 /= 10
        power += 1
        if not isprime(temp2):
            flag = False
            break
    if flag:
        print num
        summ += num
print summ 
