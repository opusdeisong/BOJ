import calendar
import sys

T = int(sys.stdin.readline())

cnt = 0
year = 2019
while (year <= T):
    for j in range(12):
        if calendar.weekday(year, j+1, 13) == 4:
            cnt += 1
    year += 1

print(cnt)