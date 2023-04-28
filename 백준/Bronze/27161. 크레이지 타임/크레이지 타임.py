import sys
N = int(sys.stdin.readline())
streak = 1
ans = 1
for i in range(N):
    a, b = sys.stdin.readline().split()
    if a == "CLOCK":
        if int(b) == ans:
            print(ans, "YES")
        else:
            print(ans, "NO")
    elif a == "WATCH":
        if int(b) == ans:
            print(ans, "YES")
        else:
            print(ans, "NO")
    elif a == "HOURGLASS":
        if int(b) == ans:
            print(ans, "NO")
        else:
            print(ans, "NO")
            streak = -streak
    ans += streak
    if ans == 13:
        ans = 1
    if ans == 0:
        ans = 12