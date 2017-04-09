


maxlen = 0
for p in range(100, 1001):
    length_sides = []
    for a in range(1,p/3):
        b = 1
        while True:
            if a**2 + b**2 == (p-a-b)**2:
                length_sides.append([a,b,p-a-b])
                break
            elif a**2 + b**2 > (p-a-b)**2:
                break
            b += 1

    if maxlen < len(length_sides):
        maxlen = len(length_sides)
        print maxlen, p, length_sides
