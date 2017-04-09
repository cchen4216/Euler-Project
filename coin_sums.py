
coins = set([1, 2, 5, 10, 20, 50, 100, 200])
summ = 200

count = 0
combinations = {}

def resetcombinations():
	global combinations
	for i in combinations.keys():
		combinations[i] = 0


def decompose(summ, coins):
	global count
	global combinations

	if summ!=0 and len(coins)==0:
		return 

	if summ == 0:
		count += 1
		print sorted(combinations.items())
		resetcombinations()
		return
	#print len(coins)
	if len(coins)==1:
		coin = coins.pop()
		if summ % coin == 0 :
			count += 1
			combinations[coin] = summ//coin
			print sorted(combinations.items())
			resetcombinations() 
		return
	else:
		coin = coins.pop()
		for i in range(summ//coin + 1):
			newsum = summ - i*coin 
			combinations[coin] = i 
			decompose(newsum, coins.copy())  #参数summ也是指针传递，递归函数的使用要小心
			# 我一直认为单个整型数据应该是指传递的，这里有些不明白。


decompose(summ, coins)
print count 