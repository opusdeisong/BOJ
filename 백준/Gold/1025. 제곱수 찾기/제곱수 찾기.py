import sys, math

N, M = map(int, sys.stdin.readline().split())
num = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

ans = -1
for i in range(N):
    for j in range(M):
        for k in range(-N, N):
            for l in range(-M, M):
                temp = ''
                x, y = i, j
                if k == 0 and l == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    temp += str(num[x][y])
                    if int(math.sqrt(int(temp))) ** 2 == int(temp):
                        ans = max(int(temp), ans)
                    x += k
                    y+= l
print(ans)