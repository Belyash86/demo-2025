f = open('files/Задание 26/demo_2025_26.txt')
n = int(f.readline())
l = [list(map(int, f.readline().split())) for _ in range(n)]
l = sorted(l, key=lambda x: (x.count(2), -sum(x[1:]), x[0]))
bad_guys = [r for r in l if r.count(2) > 2]
print(l[n//4-1][0], bad_guys[0][0])