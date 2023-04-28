def d(n):
    ans = n
    while n > 0:
        ans += n % 10
        n = n // 10
    return ans
list = []
ans = 1
while ans < 10000:
    list.append(d(ans))
    ans += 1
i = 1
while i < 10000:
    if i not in list:
        print(i)
    i += 1