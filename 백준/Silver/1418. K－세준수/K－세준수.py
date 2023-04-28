import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

K = [0 for i in range(N + 1)]

for i in range(2, N + 1):
    if K[i] == 0:
        for j in range(i, N + 1, i):
            if j % i == 0:
                K[j] = max(K[j], i)
ans = 0
for i in K:
    if i <= M:
        ans += 1
        
print(ans - 1)