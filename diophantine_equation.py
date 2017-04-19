from math import sqrt

maxd = 0
maxx = 0

for d in range(2,1001):
  temp = int(sqrt(d))
  if temp*temp==d or (temp+1)**2==d: continue
  print d

  y = 1
  while True:
    temp = int(sqrt(d)*y) + 1
    if temp*temp == y*y*d + 1 : break
    y += 1

  if maxx < temp :
    maxx = temp
    maxd = d
    print(maxd, maxx)

#print(maxd, maxx)
