def d(s1, s2):
    return ((s2[0]-s1[0])**2 + (s2[1]-s1[1])**2)**0.5
f =open('27A.txt')
f.readline()
l = [[float(x.replace(',','.')) for x in s.split()] for s in f]
clusters = [[x for x in l if x[1] < 3], [x for x in l if x[1] > 3]]
centroids = [[],[]]
for cl in clusters:
    min_dist = float('inf')
    for c in cl:
        dist = sum(d(c, star) for star in cl)
        if dist < min_dist:
            min_dist = dist
            centroids[clusters.index(cl)] = c
print(int((centroids[0][0]+centroids[1][0])/2*10000), int((centroids[0][1]+centroids[1][1])/2*10000))