import sys

T = int(sys.stdin.readline())
if T != 1:
    snow = list(map(int, sys.stdin.readline().split()))
else:
    snow = [int(sys.stdin.readline())]

time = 0

while len(snow) != 0:

    snow.sort()
    snow.reverse()
    if len(snow) == 1:
        snow[0] = snow[0] - 1
        time += 1
    else:
        snow[0] = snow[0] - 1
        snow[1] = snow[1] - 1
        time += 1
    while(0 in snow):
        snow.remove(0)


if time <= 1440:
    print(time)
else:
    print(-1)