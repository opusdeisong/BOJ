import sys

N, M = map(int, sys.stdin.readline().split())
list = [0] * (N+M)
S = sys.stdin.readline().split()
j = 0
for i in S:
    list[j] += int(i)
    j += 1
k = 0
for _ in range(N):
    temp = sys.stdin.readline().split()
    m = 0
    for l in temp:
        list[m] += int(l)
        list[k] -= int(l)
        m += 1
    k += 1

for a in list:
    print(f"{a} ", end = "")