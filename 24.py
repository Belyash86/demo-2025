import re
f = open('files/Задание 24/demo_2025_24.txt').readline()
# f = '-0678*78-896*67'
expr = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*', f)
expr_len = [len(x) for x in expr]
print(max(expr_len))