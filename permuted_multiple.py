
def get_digits(num):
    digits = []
    while num != 0:
        digits.append(num%10)
        num /= 10
    digits.reverse()
    return digits

for i in range(100, 1000000):
    ds1 = sorted(get_digits(i))
    ds2 = sorted(get_digits(2*i))
    ds3 = sorted(get_digits(3*i))
    ds4 = sorted(get_digits(4*i))
    ds5 = sorted(get_digits(5*i))
    ds6 = sorted(get_digits(6*i))
    if ds1==ds2==ds3==ds4==ds5==ds6:
        print i, 2*i, 3*i, 4*i, 5*i, 6*i
        quit()
