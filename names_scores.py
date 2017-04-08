
fobj = open('p022_names.txt')
names = fobj.read().split(',')
for i in range(len(names)):
	names[i] = names[i][1:-1]
names = sorted(names)

abDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 
'h':8,'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 
'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 
'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

#print names[937]

summ = 0
for i in range(len(names)):
	summ2 = 0
	for j in names[i].lower():
		summ2 += abDict[j]
	summ += summ2*(i+1)

print summ 