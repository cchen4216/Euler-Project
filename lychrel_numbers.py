
def reverse_digits(n):
    num = 0
    while n != 0:
        num = num*10 + n%10
        n /= 10
    return num

#print reverse_digits(1234)

lychrel_count = 0
for i in range(1,10000):
    temp = i
    flag = True
    for k in range(50):
        temp = temp + reverse_digits(temp)
        if temp == reverse_digits(temp):
            flag = False
            break
    if flag:
        lychrel_count += 1

print lychrel_count
