




for d1 in range(0,10):
    for d2 in range(10):
        for d3 in range(10):
            if (d1*10+d2)*d3 == (d1*10+d3)*d2:
                if d1*10+d2>10 and d1*10+d3>10 and d1*10+d2!=d1*10+d3:
                    if d1*10+d2 < d1*10+d3:
                        print d1*10+d2, d1*10+d3
            if (d1+d2*10)*d3 == (d1*10+d3)*d2:
                if d1+d2*10>10 and d1*10+d3>10 and d1+d2*10!=d1*10+d3:
                    if d1+d2*10 < d1*10+d3:
                        print d1+d2*10, d1*10+d3
            if (d1*10+d2)*d3 == (d1+d3*10)*d2:
                if d1*10+d2>10 and d1+d3*10>10 and d1*10+d2!=d1+d3*10:
                    if d1*10+d2 < d1+d3*10:
                        print d1*10+d2, d1+d3*10
            if (d1+d2*10)*d3 == (d1+d3*10)*d2:
                if d1+d2*10>10 and d1+d3*10>10 and d1+d2*10!=d1+d3*10 and d1!=0:
                    if d1+d2*10 < d1+d3*10:
                        print d1+d2*10, d1+d3*10


# result is 100 
