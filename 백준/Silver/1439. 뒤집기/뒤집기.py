import sys

num = str(input())
temp = int(num[0])
cnt = 0
for i in str(num):
    if temp != int(i):
        cnt += 1
    temp = int(i)
print(round(cnt / 2 + 0.4))