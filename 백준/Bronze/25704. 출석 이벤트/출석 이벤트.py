import sys

N = int(sys.stdin.readline())
P = int(sys.stdin.readline())
if N < 5:
    print(P)
elif N < 10:
    if P < 500:
        P = 500
    print(P - 500)
elif N < 15:
    if P < 500:
        P = 500
    print(min(P // 10 * 9, P - 500))
elif N < 20:
    if P < 2000:
        P = 2000
    print(min(P // 10 * 9, P - 2000))
else:
    if P < 2000:
        P = 2000
    print(min(P // 4 * 3, P - 2000))