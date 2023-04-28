def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
    return temp
T = int(input())
for i in range(T):
    n1, n2 = map(int, input().split())
    ans = fact(n2) // (fact(n1) * fact(n2 - n1))
    print(ans)