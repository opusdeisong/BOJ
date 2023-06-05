import sys

ans = 0
for _ in range(int(sys.stdin.readline())):
    ans += int(sys.stdin.readline()) - 1
print(ans + 1)