import sys

max_score = 0
winner = 0

for i in range(1, 6):
    score = sum(map(int, sys.stdin.readline().split()))
    if score > max_score:
        max_score = score
        winner = i

print(winner, max_score)
