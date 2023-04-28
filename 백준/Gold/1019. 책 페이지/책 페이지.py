import sys

N = int(sys.stdin.readline())
ans = [0 for _ in range(10)]
temp = 1
while N != 0:
    while N % 10 != 9:
        for i in str(N):
            ans[int(i)] += temp
        N -= 1
    if N < 10:
        for i in range(N + 1):
            ans[i] += temp
        ans[0] -= temp
        break
    else:
        for i in range(10):
            ans[i] += (N // 10 + 1) * temp
    ans[0] -= temp
    temp *= 10
    N = N // 10

print(*ans)
