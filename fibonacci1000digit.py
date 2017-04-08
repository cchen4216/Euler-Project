

count = 2
f1 = 1
f2 = 1

while True:
	f3 = f1 + f2
	count += 1
	if f3//(10**999) != 0:
		print count, f3//(10**999)
		quit()

	f1, f2 = f2, f3