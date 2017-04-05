
from math import sqrt

def isprime(num):
	a = int(sqrt(num)) + 1    # at first I forgot to plus 1 !!!! 
	if num%2==0:
		return False

	for i in range(3,a,2):
		if num%i == 0:
			return False
	return True

primes = [2,3]
num = 4
while len(primes)<10001:
	if isprime(num):
		primes.append(num)
	num += 1

print len(primes)
print primes[-1]