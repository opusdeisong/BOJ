import sys
from collections import deque


K = int(sys.stdin.readline())
N = int(sys.stdin.readline())
question_data = []
for _ in range(N):
    x, y = map(str, sys.stdin.readline().split())
    question_data.append((int(x), y))

time_limit = 210
players = deque(range(1, 9))
while players[0] != K:
    players.rotate(-1)

total_time = 0
for time, answer in question_data:
    total_time += time
    if total_time >= time_limit:
        break
    if answer == 'T':
        players.rotate(-1)

print(players[0])