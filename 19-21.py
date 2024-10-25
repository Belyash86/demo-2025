from functools import lru_cache
def moves(h):
    return h-2, h-5, h//3

@lru_cache(None)
def game(h):
    if h <= 19: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'П1'
    if all(game(x) == 'П1' for x in moves(h)): return 'В1'
    if any(game(x) == 'В1' for x in moves(h)): return 'П2'
    if all(game(x) in ['П1','П2']  for x in moves(h)): return 'В2'

for s in range(20, 100+1):
    g = game(s)
    if g != None:
        print(s, g)