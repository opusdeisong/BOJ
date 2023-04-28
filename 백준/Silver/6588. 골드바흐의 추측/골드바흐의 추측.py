import sys

dp = [1] * (1000000 + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, 1001):
    if dp[i]:
        for j in range(i * i, 1000001, i):
            dp[j] = 0

def check_goldbach(n):
    for i in range(2, n):
        if dp[i] and dp[n - i]: # e.g. 20 = 3 (i) + 17 (n - i)
            print(f'{n} = {i} + {n - i}')
            return 0
    return 1

while 1:
    try:
        n = int(sys.stdin.readline())
        if n == 0: 
            break
        if check_goldbach(n):
            print("Goldbach's conjecture is wrong.")
    except EOFError:
        break