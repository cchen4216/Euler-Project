

def digits10(num):
    digits = []
    while num != 0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits

def digits2(num):
    digits = []
    while num != 0:
        digits.append(num%2)
        num /= 2
    digits.reverse()
    return digits


#print digits2(13)
palindromes = []
for i in range(1, 1000000):
    list1 = digits10(i)
    list2 = list1[:]; list2.reverse()
    if list1 == list2:
        list1 = digits2(i)
        list2 = list1[:]; list2.reverse()
        if list1 == list2:
            print i,
            palindromes.append(i)

print ''
print sum(palindromes)
