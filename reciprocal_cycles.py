import math 

def calc_cycle_len(num):
	largenumber = 10**8010
	
	#temp = float(largenumber)/float(num)
	#if temp%1 == 0:  # no recurring cycle
	#	return 0 

	temp = largenumber/int(num)
	digits = []
	while temp!=0:
		digits.append(int(temp%10))
		temp /= 10
	#print digits
	flag = True
	for i in range(1, 4001):
		if digits[:i]==digits[i:2*i]: #and digits[:2*i]==digits[2*i:4*i]:
			flag = False
			#print digits[:i]
			#print digits[i:2*i]
			return i 
	if flag:
		print num, 'cycle length longer than 4000'
		return 4000



#print calc_cycle_len(97)
#quit()


maxlen = 0 
for i in range(1,1000):
	temp = calc_cycle_len(i)
	if temp>maxlen:
		maxlen = temp
		print i, maxlen

print ''
print 'maxlen =', maxlen

