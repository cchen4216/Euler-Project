def calc_len(num):

 	count = 1
 	while num != 1:
 		if num%2==0:
 			num /= 2
 		else:
 			num = 3*num+1
 		count += 1
 	return count

print calc_len(13)

maxlen = 0
start = 0
for i in range(10,1000000):
 	lens = calc_len(i)
 	if lens>maxlen:
 		maxlen = lens
 		start = i

print maxlen, start