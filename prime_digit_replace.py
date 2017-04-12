
from math import sqrt

def isprime(num):
    a = int(sqrt(num))
    if num<2: return False
    if num==2: return True
    if num%2==0: return False
    for i in range(3,a+1,2):
        if num%i==0: return False
    return True

def check_replacement(num):
    n = num
    digits = []
    while n != 0:
        digits.append(n%10)
        n /= 10
    digits.reverse()

    for length in range(1,len(digits)):
        for i in range(len(digits)-length+1):
            select = [i]
            if length == 1:
                replace_check(digits, select)
                continue
            temp = []
            for j in range(i+1,len(digits)):
                if digits[j]==digits[i]:
                    temp.append(j)
                    if len(temp)==length-1: break
            select.extend(temp)
            if len(select)==length:
                replace_check(digits, select)


def replace_check(digits, select):
    dgts = digits[:]
    select = sorted(select)
    old_digit = dgts[select[0]]

    count = 1
    list1 = []
    for k in range(1,10):
        new_digit = (old_digit + k) % 10
        if select[0]==0 and new_digit==0:
            continue
        for i in select: dgts[i] = new_digit
        n = 0
        for i in dgts:
            n = n*10 + i
        if isprime(n):
            count += 1
            list1.append(n)
    if count == 8:
        print digits, list1
        quit() 

for n in range(60000, 1000000):
    if not isprime(n): continue
    check_replacement(n)
    #print n
