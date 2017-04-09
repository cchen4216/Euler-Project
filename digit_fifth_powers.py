
import numpy as np 

def get_digits(num):
	digits = []
	while num!=0:
		digits.append(num%10)
		num = num//10 
	return digits

#print get_digits(1234)
summ = 0
for i in range(2,1000000):
	digits = np.array(get_digits(i))
	if i == sum(digits**5):
		summ += i 
		print i, summ 


