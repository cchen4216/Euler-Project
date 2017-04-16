
P3s = []
P4s = []
P5s = []
P6s = []
P7s = []
P8s = []

n = 1
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
while True:
    temp = n*(n+1)/2
    if 999<temp<10000: P3s.append(temp)
    if temp>9999: flag1 = True
    temp = n*n
    if 999<temp<10000: P4s.append(temp)
    if temp>9999: flag2 = True
    temp = n*(3*n-1)/2
    if 999<temp<10000: P5s.append(temp)
    if temp>9999: flag3 = True
    temp = n*(2*n-1)
    if 999<temp<10000: P6s.append(temp)
    if temp>9999: flag4 = True
    temp = n*(5*n-3)/2
    if 999<temp<10000: P7s.append(temp)
    if temp>9999: flag5 = True
    temp = n*(3*n-2)
    if 999<temp<10000: P8s.append(temp)
    if temp>9999: flag6 = True
    n += 1
    if flag1 and flag2 and flag3 and flag4 and flag5 and flag6:
        break


ps = [P3s, P4s, P5s, P6s, P7s, P8s]
flag = False
num0 = 0
results = []
def find_cyclic(pss, num1):
    global flag, num0, results
    #print len(pss),
    if len(pss) == 1:
        for i in pss[0]:
            if i/100 != num1: continue
            if i%100 != num0: continue
            results.append(i)
            print results, sum(results)
            flag = True
            quit()
        results = results[:-1]
    else:
        for ips in range(len(pss)):
            for i in pss[ips]:
                if i/100 != num1 and len(pss)!=6: continue
                if len(pss)==6: num0 = i/100
                results.append(i)
                find_cyclic(pss[:ips]+pss[ips+1:], i%100)
        results = results[:-1]


find_cyclic(ps, 0)
