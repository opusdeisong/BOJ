import sys

N, M = map(int, sys.stdin.readline().split())
listt = []
ans = []
for _ in range(N):
    temp = sys.stdin.readline().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    listt.append(temp)
if M != 0 and N != 1:
    if (M <=  N):
        M = M - 1
    else:
        M = (M - 1) % N + N

    for _ in range(M + 1):
        inst = 0
        moved = 0
        for i in range(N):
            if i == 0:
                listt[i].sort()
                inst = listt[i][0]
                moved = 0
            else:
                listt[i].sort()
                listt[i-1][moved] = listt[i][1]
                moved = 1
        listt[i][1] = inst

for i in listt:
    i.sort()
    print(f"{i[0]} {i[1]}")

