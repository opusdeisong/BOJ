import sys

case = 1
while True:
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    if n == 0:
        break
    data = data[1:]
    if n % 2 == 1:
        median = data[n//2]
    else:
        median = (data[n//2 - 1] + data[n//2]) / 2
    print('Case {}: {:.1f}'.format(case, median))
    case += 1
