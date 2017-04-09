from math import sqrt
pandigits = [1,2,3,4,5,6,7,8,9]
pannum = 0

def isprime(num):
    a = int(sqrt(num))
    if num%2 == 0 or num==1:
        return False
    if num==2:
        return True
    for i in range(3,a+1,2):
        if num%i == 0:
            return False
    return True
#print isprime(14)

def get_pannums(digits):
    global pannum, testnum
    digits = sorted(digits, reverse=True)
    if len(digits) == 1:
        pannum = pannum*10 + digits[0]
        #print pannum
        if isprime(pannum):
            print pannum
            quit()
        pannum /= 10
        return
    for i in digits:
        pannum = pannum*10 + i
        temp = digits[:]
        temp.remove(i)
        get_pannums(temp)
        pannum /= 10

for i in range(len(pandigits), 1, -1):
    get_pannums(pandigits[:i])
