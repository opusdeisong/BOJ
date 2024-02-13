def check(A, B, C):
    if C[1] > B[1] or C[1] <= A[1]:
        return False
    return (B[1] - A[1]) * C[0] < (B[1] - C[1]) * A[0] + (C[1] - A[1]) * B[0]

N = int(input())
d = [tuple(map(int, input().split())) for _ in range(N)]
d.sort(key=lambda x: x[1])  

cnt = [[0 for _ in range(N)] for _ in range(N)]
ans = [0 for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if check(d[i], d[j], d[k]):
                cnt[i][j] += 1

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if check(d[i], d[k], d[j]):
                x = cnt[i][k] - 1 - cnt[i][j] - cnt[j][k]
                if check(d[i], d[j], d[k]):
                    x += 1
                if check(d[j], d[k], d[i]):
                    x += 1
            else:
                x = cnt[i][j] + cnt[j][k] - cnt[i][k]
                if check(d[i], d[j], d[k]):
                    x -= 1
                if check(d[j], d[k], d[i]):
                    x -= 1
            ans[x] += 1

for i in range(N - 3 + 1):
    print(ans[i])