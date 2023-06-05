import sys

M = int(sys.stdin.readline())
ball_position = 1

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    if X == ball_position:
        ball_position = Y
    elif Y == ball_position:
        ball_position = X

print(ball_position)
