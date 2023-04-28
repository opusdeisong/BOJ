import sys
T = sys.stdin.readline()

for i in T:
    if i == i.upper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')