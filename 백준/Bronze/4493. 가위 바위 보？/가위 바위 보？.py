import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    p1, p2 = 0, 0
    for _ in range(n):
        a, b = sys.stdin.readline().split()
        if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
            p1 += 1
        elif a != b:
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")
