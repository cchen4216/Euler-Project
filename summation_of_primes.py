from math import sqrt 

def isprime(num):
	a = int(sqrt(num)) + 1

	if num%2 == 0:
		return False

	for i in range(3,a,2):
		if num%i == 0:
			return False

	return True 

primes = [2,3]
num = 5
while num < 2000000:
	if isprime(num):
		primes.append(num)
	num += 2

print sum(primes)
print len(primes)