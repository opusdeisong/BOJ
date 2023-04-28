def fact(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i

    return temp
N = int(input())
ans = fact(N)
i = 0
while ans % 10 == 0:
    ans = ans // 10
    i += 1

print(i)