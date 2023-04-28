import sys
import math
n = int(sys.stdin.readline())
ans = n
num = []
for i in range(2, round(n ** 0.5) + 1):
    if n % i == 0:
        while n % i == 0:
            n //= i
        num.append(i)
if n > 1:
    num.append(n)
for i in num:
    ans *= 1 - (1 / i)
print(round(ans))