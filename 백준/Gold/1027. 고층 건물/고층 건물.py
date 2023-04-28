import sys

N = int(sys.stdin.readline())
building = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(N):
    temp = 0
    height = building[i]
    for j in range(N):
        dx = j - i
        dy = height - building[j]
        if dx != 0:
            d = dy / abs(dx)
            k = 1
            if dx > 0:
                k = -1
            b = 1
            for l in range(j + k, i, k):
                if building[l] >= building[j] + d * abs(l - j):
                    b = 0
                    break
            if b:
                temp += 1
    ans = max(ans, temp)
print(ans)