
def count_divisor(num):
# this method is extremely time consuming 
	count = 0 
	for i in range(1,num+1):
		if num % i == 0:
			count += 1
	return count 

def count_divisor2(num):
	lower = 1
	upper = num
	count = 0
	while lower<upper :
		if num % lower == 0 :
			count += 2
			upper = num/lower
			if upper == lower:
				count -= 1
		lower += 1

	return count 


#print count_divisor2(28)

i = 1
tri_num = 0
while True:
	tri_num += i 
	i += 1
	temp = count_divisor2(tri_num)
	if temp > 500:
		print tri_num
		break

