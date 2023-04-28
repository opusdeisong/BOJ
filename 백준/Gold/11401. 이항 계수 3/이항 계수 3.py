N, K = map(int, input().split())
P = 1000000007

def factorial(num, mod):
    result = 1
    for i in range(2, num + 1):
        result = result * i % P
    return result

def power(num, p, mod):
    if p == 1:
        return num % mod

    if p % 2:
        return ((power(num, p // 2, mod) ** 2) * num) % mod
    else:
        return (power(num, p // 2, mod) ** 2) % mod

print(factorial(N, P) * power((factorial(K, P) * factorial(N - K, P)), P - 2, P) % P)