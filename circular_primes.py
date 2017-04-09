from math import sqrt

def isprime(num):
    a = int(sqrt(num))

    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3, a+1, 2):
        if num%i == 0:
            return False
    return True

def rotate_nums(digits):
    nums = []
    length = len(digits)
    if length == 1:
        return None
    for i in range(1, length):
        list1 = digits[i:] + digits[:i]
        num = 0
        for j in list1:
            num = num*10 + j
        nums.append(num)
    return nums
#print rotate_nums([1,2,3,4])

def get_digits(num):
    digits = []
    while num != 0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits
#print get_digits(1234)

cycle_primes = []
for num in range(2, 1000000):
    if isprime(num):
        digits = get_digits(num)
        if 0 in digits:
            continue
        nums = rotate_nums(digits)
        if nums==None:
            #print num
            cycle_primes.append(num)
            continue
        flag = True
        for i in nums:
            if not isprime(i):
                flag = False
        if flag:
            #print num
            cycle_primes.append(num)

print cycle_primes
print len(cycle_primes)
