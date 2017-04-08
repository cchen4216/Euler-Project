
count = 0
maxDigit = 10
digits = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

def assign_digit(idx):
	global maxDigit
	global count 
	global digits

	for i in range(maxDigit):
		if i in digits:
			continue
		digits[idx] = i

		if idx==maxDigit-1:
			count += 1
			#print count, digits
			if count==1000000:
				print digits
			digits[idx] = -1
			return

		assign_digit(idx+1)
		digits[idx] = -1

assign_digit(0)

