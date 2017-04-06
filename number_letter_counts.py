letters = {}
letters[1] = 3
letters[2] = 3
letters[3] = 5
letters[4] = 4
letters[5] = 4
letters[6] = 3
letters[7] = 5
letters[8] = 5
letters[9] = 4
letters[10] = 3
letters[11] = 6
letters[12] = 6
letters[13] = 8
letters[14] = 8
letters[15] = 7
letters[16] = 7
letters[17] = 9
letters[18] = 8
letters[19] = 8
letters[20] = 6
letters[30] = 6
letters[40] = 5
letters[50] = 5
letters[60] = 5
letters[70] = 7
letters[80] = 6
letters[90] = 6
 
def count_letter(num):
# num less than 1000
	global letters
	count = 0
	if num > 100:
		count += 10  # hundred and = 10
		count += letters[num//100]
		num %= 100
	elif num == 100:
		return 10    # one hundred

	if num == 0:
		return count-3

	if num <= 20:
		return count + letters[num]

	count += letters[10*(num//10)]
	num = num%10
	if num!=0:
		count += letters[num]
	return count 

print count_letter(115)
summ = 0
for i in range(1,1000):
	summ += count_letter(i)

summ += 11    # one thousand

print summ 




