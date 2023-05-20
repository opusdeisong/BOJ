import sys

ans = 0
while True:
    temp = int(sys.stdin.readline())
    if temp == -1:
        break
    ans += temp
print(ans)