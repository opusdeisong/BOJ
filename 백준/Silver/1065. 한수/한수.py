N = int(input())

i = 1
ans = 0
while i <= N:
    temp = i
    list = []
    if temp <= 99:
        ans += 1
    elif temp == 1000:
        ans = 144
    else:
        while temp > 0:
            list.append(temp % 10)
            temp = temp // 10
        if list[0] - list[1] == list[1] - list[2]:
            ans += 1
    i += 1

print(ans)