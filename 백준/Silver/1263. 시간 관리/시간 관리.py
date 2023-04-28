import sys

N = int(sys.stdin.readline())
T_S = [0 for z in range(N)]

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    temp. reverse()
    T_S[_] = temp
T_S.sort()
T_S.reverse()
ans = T_S[0][0] - T_S[0][1]

for i in range(1, N):
    if ans > T_S[i][0]:
        ans = T_S[i][0] - T_S[i][1]
    else:
        ans -= T_S[i][1]
if ans >= 0:
    print(ans)
else:
    print(-1)