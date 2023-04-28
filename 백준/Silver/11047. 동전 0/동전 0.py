import sys
N, K = map(int, sys.stdin.readline().split())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
j = 0
num.sort(reverse=True)
for i in num:
    j += K // i
    K = K % i

print(j)