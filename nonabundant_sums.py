

def calc_divisors(num):
	divisors = [1]
	lower = 2
	upper = num
	while lower<upper:
		if num%lower==0:
			divisors.append(lower)
			upper = num/lower
			if upper!=lower:
				divisors.append(upper)
		lower += 1
	return divisors 

#print calc_divisors(28)

## create abundant number list for integers less than 28123
abundant_nums = []
for i in range(10, 28123+1):
	if i<sum(calc_divisors(i)):
		abundant_nums.append(i)

#print abundant_nums[:20]
#print len(abundant_nums)

## calculate the summation of non-abundant sums
abundant_nums = sorted(abundant_nums)
summation = 0
for num in range(1, 28123+1):
	flag = True
	for i in abundant_nums:
		if i>num:
			break
		if (num-i) in abundant_nums:
			flag = False
			break 
	if flag:
		summation += num  
		print num, summation

print summation
