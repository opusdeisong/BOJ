import sys

n = sys.stdin.readline().rstrip()
ans = len(n)
for i in n:
    if i == ':':
        ans += 1
    elif i == "_":
        ans += 5
print(ans)