import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    stu = [list(map(int, sys.stdin.readline().split())) for __ in range(M)]
    stu.sort(key= lambda x: x[1])
    cnt = 0
    temp = [0] * (N + 1)

    for a, b in stu:
        for i in range(a, b + 1):
            if temp[i] == 0:
                temp[i] = 1
                cnt += 1
                break

    print(cnt)