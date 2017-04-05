
from math import sqrt


def isprime(num):
	a = int(sqrt(num))
	if num % 2 == 0:
		return False

	for i in range(3, a, 2):
		if num % i == 0:
			return False
	return True


num = 600851475143
a = int(sqrt(num))
#print a

for i in range(a, 2, -1):
	if num % i == 0 and isprime(i):
		print i 
		break
