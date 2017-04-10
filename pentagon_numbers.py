
from math import sqrt
pentagons = []

def check_sum_pentagon(num):
    a = int(sqrt(num))
    for i in range(1,a+1):
        if 2*num == i*(3*i-1):
            return True
    return False

for n in range(1,50000):
    num = n * (3*n-1) / 2
    for i in pentagons[-1::-1]:
        # check if the difference is pentagon
        if num-i in pentagons:
            #print i, num
            # check if the sum is pentagon
            if check_sum_pentagon(i+num):
                print i, num
                quit()
    pentagons.append(num)

#print pentagons
