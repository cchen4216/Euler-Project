import numpy as np 


a = np.zeros((1001, 1001))
#print a.shape 

i = 500
j = 500
count = 1

a[i][j] = count
count += 1
for k in range(1,501):
	for n in range(-k+1,k+1):
		a[i+n, j+k] = count
		count += 1
	#print a 
	for n in range(k-1, -k-1, -1):
		a[i+k, j+n] = count
		count += 1
	#print a 
	for n in range(k-1, -k-1, -1):
		a[i+n, j-k] = count
		count += 1
	#print a 
	for n in range(-k+1, k+1):
		a[i-k, j+n] = count
		count += 1
	#print a 

#print a 
summ1 = 0
for n in range(1001):
	summ1 += a[n][n]
print summ1 
summ2 = 0 
for n in range(1001):
	summ2 += a[1000-n][n]
print summ2
print summ1 + summ2 -1 
