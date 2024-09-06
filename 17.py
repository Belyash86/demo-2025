l = [int(x) for x in open('files/Задание 17/demo_2025_17.txt')]
k, max_sum = 0, 0
for i in range(len(l)-1):
    if l[i]%16 == min(l) or l[i+1]%16 == min(l):
        k += 1
        max_sum = max(max_sum, l[i]+l[i+1])
print(k, max_sum)