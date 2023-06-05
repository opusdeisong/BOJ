import sys

n, T = map(int, sys.stdin.readline().split())
tasks = list(map(int, sys.stdin.readline().split()))

count = 0
time = 0
for task in tasks:
    if time + task <= T:
        time += task
        count += 1
    else:
        break

print(count)
