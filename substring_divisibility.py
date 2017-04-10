

pandigits = [0,1,2,3,4,5,6,7,8,9]
primes = [2,3,5,7,11,13,17]
divi_num = 0
divisibles = []

def isdivisible(num):
    global primes
    for i in range(7):
        temp = num / 10**i
        temp %= 1000
        if temp % primes[-(i+1)] != 0:
            return False
    return True
#print isdivisible(1406357289)
#print isdivisible(1406357298)
#quit()

def get_pan_nums(digits):
    global divi_num, divisibles
    if len(digits)==1:
        divi_num = divi_num*10 + digits[0]

        #check property
        if isdivisible(divi_num):
            print divi_num
            divisibles.append(divi_num)

        divi_num /= 10
        return
    start = 1 if len(digits)==10 else 0
    for i in digits[start:] :
        divi_num = divi_num*10 + i
        temp = digits[:]
        temp.remove(i)
        get_pan_nums(temp)
        divi_num /= 10

get_pan_nums(pandigits)
print sum(divisibles)
