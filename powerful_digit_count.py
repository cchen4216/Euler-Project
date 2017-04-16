
def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n /= 10
    return count
#print count_digits(1234)
#quit()



power = 1
count = 0

while power < 33 :
    for i in range(1,10):
        if count_digits(i**power) == power :
            count += 1
            print i, power, i**power
    power += 1

print count
