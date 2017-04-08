
def calc_divisors(num):
	divisors = [1]
	lower = 2
	upper = num
	while lower<upper:
		if num%lower == 0:
			divisors.append(lower)
			upper = num/lower
			if lower != upper:
				divisors.append(upper)
		lower += 1
	return divisors

summ = 0
for i in range(2,10000):
	a = sum(calc_divisors(i))
	if a!=i and a<10000 and i==sum(calc_divisors(a)):
		summ = summ + i + a
		#print i, a  

print summ/2


