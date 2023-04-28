N ,K = map(int, input().split())

count = 0
hour = ""
minute = ""
second = ""
for i in range(N + 1):
    if i < 10:
        hour = "0" + str(i)
    else:
        hour = str(i)
    for j in range(60):
        if j < 10:
            minute = "0" + str(j)
        else:
            minute = str(j)
        for k in range(60):
            if k < 10:
                second = "0" + str(k)
            else:
                second = str(k)
            if str(K) in hour or str(K) in minute or str(K) in second:
                count += 1

print(count)