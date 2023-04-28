import sys


T = sys.stdin.readline()
temp = T[0]
cnt = 0
for i in T:
    if temp == i:
        cnt += 1
    else:
        break
print(cnt)