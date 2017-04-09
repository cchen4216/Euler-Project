


def get_digits(num):
    digits = []
    if num== 0:
        return [0]
    while num != 0 :
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits

i = 1
frac_digits = []
while len(frac_digits) < 1000000 :
    frac_digits.extend(get_digits(i))
    i += 1

#print frac_digits
print frac_digits[0]*frac_digits[9]*frac_digits[99]*frac_digits[999]\
*frac_digits[9999]*frac_digits[99999]*frac_digits[999999]
