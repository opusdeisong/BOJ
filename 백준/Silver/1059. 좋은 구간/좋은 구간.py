T = int(input())

temp = list(map(int, input().split()))
temp.sort()
N = int(input())
if N in temp:
    print(0)
else:
    cnt = 0
    for i in range(len(temp)):
        if temp[i] > N:
            big = temp[i]
            small = temp[i - 1]
            if i == 0:
                small = 1
                for i in range(small, N + 1):
                    for j in range(N, big):
                        cnt += 1
            else:
                for i in range(small + 1, N + 1):
                    for j in range(N, big):
                        cnt += 1
            break


    print(cnt - 1)