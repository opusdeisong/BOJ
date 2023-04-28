import sys, math

N = int(sys.stdin.readline())
temp = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]
star = [[' ' for _ in range(N * 2)] for _ in range(N)]



def recursive(x, y, n):
    if n <= 3:
        for i in range(3):
            for j in range(i+1):
                star[x + i][y + j] = star[x + i][y - j] = '*'
        star[x+1][y] = ' '
        return
    recursive(x, y, n // 2)
    recursive(x + n // 2, y - n // 2, n // 2)
    recursive(x + n // 2, y + n // 2, n // 2)


recursive(0, N - 1, N)

for i in range(N):
    print("".join(star[i]))