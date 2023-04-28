import sys

N = int(sys.stdin.readline())
sum = 0
for _ in range(N):
    temp = int(sys.stdin.readline())
    sum += temp
print(sum)