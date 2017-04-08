from math import sqrt

def isprime(num):
	if num<=0 :
		return False 
	a = int(sqrt(num))

	if num==2:
		return True
	elif num%2 == 0:
		return False

	for i in range(3, a+1, 2):
		if num%i == 0:
			return False
	return True

def primes1000():
	primes = []
	for i in range(2,1001):
		if isprime(i):
			primes.append(i)
	return primes 

primes = primes1000()
#print len(primes)

maxlen = 0
for b in primes:
	for a in range(-999, 1000):
		count = 1
		n = 1
		while True:
			if isprime(n*n + a*n + b):
				n += 1
				count += 1
			else:
				break 
		if maxlen < count:
			maxlen = count 
			print maxlen, a, b 




