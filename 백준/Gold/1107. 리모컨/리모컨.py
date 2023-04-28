N = int(input())
M = int(input())

if M != 0:
    wrong = list(map(int, input().split()))
else:
    wrong = []
num = 100

ans = abs(N - 100)
for i in range(1000000):
    numArr = list(str(i))
    flag = False

    for k in numArr:
        if int(k) in wrong:
            flag = True
            break

    if flag:
        continue

    else:
        ans = min(ans, abs(N - i) + len(str(i)))

print(ans)