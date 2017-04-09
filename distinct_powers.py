
powers = []
for a in range(2,101):
	for b in range(2,101):
		powers.append(a**b)

print len(powers)
powers = set(powers)
print len(powers)