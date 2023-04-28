import sys

N = int(sys.stdin.readline())
coin = [list(sys.stdin.readline()) for _ in range(N)]
res = N * N + 1

for bit in range(1 << N):
    temp = [coin[i][:] for i in range(N)]
    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if temp[i][j] == 'H':
                    temp[i][j] = 'T'
                else:
                    temp[i][j] = 'H'

    sum = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if temp[j][i] == 'T':
                cnt += 1
        sum += min(cnt, N - cnt)
    res = min(res, sum)
print(res)