
def ispalindromic(num):
	a = 0
	b = num 
	while num//10 != 0:
		a = 10*a + num%10
		num = num//10
	a = a*10 + num 
	#print a
	return a==b

max = 0
#print ispalindromic(12345654321)
for i in range(100,1000):
	for j in range(100,1000):
		if ispalindromic(i*j) and i*j>max :
			max = i*j
print max 