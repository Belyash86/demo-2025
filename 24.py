import re
f = open('files/Задание 24/demo_2025_24.txt').readline()
l = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*', f)
print(max(len(x) for x in l))