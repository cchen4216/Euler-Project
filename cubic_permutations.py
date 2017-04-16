from math import pow

def get_digits(n):
    list1 = []
    while n != 0:
        list1.append(n%10)
        n /= 10
    list1.reverse()
    return list1
#print get_digits(1234)
#quit()
def get_number(dgts):
    num = 0
    for i in dgts:
        num = 10*num + i
    return num
#print get_number([1,2,3,4])
#quit()
def is_cubic(num):
    temp = int(pow(num, 1./3.))
    if temp**3==num or (temp+1)**3==num :
        return True
    else:
        return False
#print is_cubic(216)
#quit()

permute_num = 0
def cubic_permute(dgts):
    global permute_num, results
    if len(dgts)==1:
        permute_num = permute_num*10 + dgts[0]
        length = len(get_digits(next(iter(results))))
        if is_cubic(permute_num) and length==len(get_digits(permute_num)):
            results.add(permute_num)
        permute_num /= 10
    else:
        for i in range(len(dgts)):
            permute_num = permute_num*10 + dgts[i]
            cubic_permute(dgts[:i]+dgts[i+1:])
            permute_num /= 10

num = 300
#results = []
while True:
    results = set([num**3])
    digits = get_digits(num**3)
    cubic_permute(digits)
    if len(results) >= 5:
        print results
        quit()
    print num
    num += 1
