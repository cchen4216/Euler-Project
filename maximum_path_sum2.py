
fobj = open('p067_triangle.txt')
trinumbers = fobj.readlines()
for i in range(len(trinumbers)):
 	trinumbers[i] = trinumbers[i].split()
for row in trinumbers:
 	for i in range(len(row)):
 		row[i] = int(row[i])
a = trinumbers
b = [(59,0,0)]

for i in range(1,100): # scan in rows
 	lenb = len(b)
 	for k in range(lenb):
 		ki = b[k][1]
 		kj = b[k][2]
 		temp = b[k][0] + a[ki+1][kj]
 		b.append((temp, ki+1, kj))
 		temp = b[k][0] + a[ki+1][kj+1]
 		b.append((temp, ki+1, kj+1))
 	for k in range(lenb-1,-1,-1):
 		del b[k]
 	if len(b) > 20000:
 		b = sorted(b, reverse=True)[:20000]

#print b
sums = []
for i in range(len(b)):
 	sums.append(b[i][0])

print len(sums)
print max(sums)