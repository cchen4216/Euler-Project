
fibs = [1, 2]

i = fibs[-1] + fibs[-2]

while i <= 4000000:
	fibs.append(i)
	i = fibs[-1] + fibs[-2]

print fibs

sum = 0
for i in fibs:
	if i%2==0:
		sum += i

print sum 