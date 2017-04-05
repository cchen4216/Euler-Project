
sum = 1000
for a in range(1,998):
	for b in range(1, sum-a):
		c = sum - a - b
		alist = sorted([a,b,c])
		if alist[0]**2 + alist[1]**2 == alist[2]**2 :
			print alist[0]*alist[1]*alist[2]
			#print alist
			break 