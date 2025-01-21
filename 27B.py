def d(s1, s2):
    return ((s2[0]-s1[0])**2 + (s2[1]-s1[1])**2)**0.5
f =open('27B.txt')
f.readline()
l = [[float(x.replace(',','.')) for x in s.split()] for s in f]
clusters = [[x for x in l if x[0] < 3 and x[1]<3], [x for x in l if x[0] > 5 and x[1] < 7], [x for x in l if x[1] > 7]]
centroids = [[],[],[]]
for n in range(3):
    cl = clusters[n]
    min_dist = float('inf')
    for i in range(len(cl)):
        dist = sum(d(cl[i], star) for star in cl)
        if dist < min_dist:
            min_dist = dist
            centroids[n] = cl[i]
print(int((centroids[0][0]+centroids[1][0]+centroids[2][0])/3*10000), int((centroids[0][1]+centroids[1][1]+centroids[2][1])/3*10000))