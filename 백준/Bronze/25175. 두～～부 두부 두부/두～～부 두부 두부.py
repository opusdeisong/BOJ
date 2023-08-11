import sys

N, M, K = map(int, sys.stdin.readline().split())

while K < 0:
    K += N
    
ans = (K - 3) % N + M

if ans > N:
    ans %= N
print(ans)