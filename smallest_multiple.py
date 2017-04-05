import numpy as np 

def divide_times(a, b):
	if a%b != 0:
		return 0
	count  = 0
	while a%b == 0:
		count += 1
		a = a/b
	return count

#print divide_times(24, 2)

# all factors from 2 to 20 for dividing check
factors = range(2,21)
# all prime numbers between 1 and 20 
primes = [2, 3, 5, 7, 11, 13, 17, 19]
times = [0, 0, 0, 0, 0, 0, 0, 0]

for factor in factors:
	for j in range(len(primes)):
		temp = divide_times(factor, primes[j])
		times[j] = temp if temp>times[j] else times[j]

primes = np.array(primes)
times = np.array(times)
print np.prod(primes**times)
