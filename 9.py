f = open('demo_2025_9.csv')
k = 0
for s in f:
    l = [int(x) for x in s.split(';')]
    # l = [1, 1, 1, 2, 5, 3]
    p, n = [], []
    for d in l:
        if l.count(d) > 1:
            p.append(d)
        else: n.append(d)
    if len(p) == 3 and (sum(p)**2 > sum(n)**2):
        k += 1
print(k)