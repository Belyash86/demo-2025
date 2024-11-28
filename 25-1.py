def m(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return i + n//i
    return 0

n = 800001
k = 0
while k < 5:
    if m(n) % 10 == 4:
        print(n, m(n))
        k += 1
    n += 1

