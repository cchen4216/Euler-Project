
liste = [2]
for i in range(1, 100):
	if i%3 == 2:
		liste.append(2*(i//3+1))
	else:
		liste.append(1)

#print(liste)

liste.reverse()
denom = liste[0]
numer = 1
for i in liste[1:-1]:
  numer = i*denom + numer
  numer, denom = denom, numer

numer = denom*liste[-1] + numer
#print(numer, denom)

summ = 0
while numer != 0:
  summ += numer%10
  numer //= 10
print(summ) 
