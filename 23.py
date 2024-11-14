def f(c, e):
    if c == e: return 1
    if c < e: return 0
    return f(c-2, e) + f(c//2, e)

print(f(38, 16)*f(16, 2))