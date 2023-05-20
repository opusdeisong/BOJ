import sys

n = sys.stdin.readline()
a = 0
b = 0
for i in n:
    if i == 'B':
        a += 1
    elif i == 'C':
        b += 1
print(a // 2 + b // 2)