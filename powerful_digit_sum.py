
def sumDigits(num):
    summ = 0
    while num != 0:
        summ += num%10
        num /= 10
    return summ

#print sumDigits(4125)
#quit()

maxSum = 0
for a in range(1,100):
    for b in range(1, 100):
        temp = sumDigits(a**b)
        maxSum = temp if maxSum<temp else maxSum
print maxSum
