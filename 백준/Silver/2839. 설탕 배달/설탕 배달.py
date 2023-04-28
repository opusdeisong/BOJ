N = int(input())

ans = 0
while N >= 0:
    if N % 5 == 0:
        print(ans + N // 5)
        break
    N -= 3
    ans += 1
else:
    print(-1)