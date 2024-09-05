for x in '0123456789ABCDEFGHI':
    res = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if res%18 == 0: print(res, x, res//18)