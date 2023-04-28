N = list(input().split())
ans = 0
for i in N:
    ans = ans + int(i) * int(i)
print(ans % 10)