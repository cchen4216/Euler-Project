

pandigits = set([1,2,3,4,5,6,7,8,9])

def get_digits(num):
    digits = []
    if num==0:
        return [0]
    while num!=0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits
#print get_digits(1234)
#quit()

def to_num(digits):
    num = 0
    for i in digits:
        num = num*10 + i
    return num
#print to_num([3,2,1])
#quit()

maxprod = 0
for i in range(1,10000):
    digits = []
    for k in range(1,10):
        list1 = get_digits(i*k)
        digits.extend(list1)
        if len(digits)==9 and set(digits)==pandigits:
            num = to_num(digits)
            if num > maxprod :
                maxprod = num
                print i, k, maxprod
            break
        elif len(digits)>9:
            break
