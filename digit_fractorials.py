
from math import factorial

def get_digits(num):
    digits = []
    while num != 0 :
        digits.append(num%10)
        num = num/10
    return digits

for num in range(4,100000):
    list1 = get_digits(num)
    summ = 0
    for i in list1:
        summ += factorial(i)
    if num == summ:
        print num

#print get_digits(1234)
