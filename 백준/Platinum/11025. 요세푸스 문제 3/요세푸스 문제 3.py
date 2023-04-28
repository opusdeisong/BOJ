import sys

N, K = map(int, sys.stdin.readline().split())

ans = 0
for i in range(1,N+1):
    ans = (ans + K)%i
print(ans + 1)