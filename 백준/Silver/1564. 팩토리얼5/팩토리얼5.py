N = int(input())
ans = 1
for i in range(1, N + 1):
    ans = ans * i
    while (ans % 10 == 0):
        ans = ans // 10
    ans = ans % 100000000000000000
print(str(ans)[-5:])