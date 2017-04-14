
def count_digit(num):
    count = 0
    while num!=0:
        count += 1
        num /= 10
    return count
#print count_digit(1)
#quit()

def next_frac(numer, denom):
    return denom, 2*denom + numer

n1 = 1
d1 = 2
count = 0
for i in range(2, 1001):
    n, d = next_frac(n1, d1)
    n1, d1 = n, d
    if count_digit(d+n) > count_digit(d):
        count += 1
    #print i, d+n, d
print count
