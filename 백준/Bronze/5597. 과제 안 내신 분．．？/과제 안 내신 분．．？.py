import sys
num = [0 for z in range(28)]
for i in range(28):
    num[i] = int(sys.stdin.readline())
for i in range(1,31):
    if i not in num:
        print(i)