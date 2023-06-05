import sys

N = int(sys.stdin.readline())

A_wins = 0
B_wins = 0

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    if A > B:
        A_wins += 1
    elif B > A:
        B_wins += 1

print(A_wins, B_wins)
