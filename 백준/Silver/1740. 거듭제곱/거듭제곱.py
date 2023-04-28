N = int(input())
num = []
ans = 0
while N > 0:
    num.append(N % 2)
    N //= 2

for i in range(len(num)):
    if num[i] == 1:
        ans += 3 ** i
print(ans)