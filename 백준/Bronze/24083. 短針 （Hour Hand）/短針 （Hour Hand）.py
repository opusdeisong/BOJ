import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
ans = (a + b) % 12
if ans == 0:
    print(12)
else:
    print(ans)