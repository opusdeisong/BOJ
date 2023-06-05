import sys

N = int(sys.stdin.readline())
count = 0
for _ in range(N):
    days = sys.stdin.readline().rstrip()
    days = days [2:]
    if int(days) <= 90:
        count += 1
print(count)

