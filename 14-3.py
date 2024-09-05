for x in range(1, 2030+1):
    res = 7**170 + 7**100 - x
    k = 0
    while res>0:
        k += res%7==0
        res //= 7
    if k == 71: print(x)