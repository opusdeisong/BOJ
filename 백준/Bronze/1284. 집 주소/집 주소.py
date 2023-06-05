import sys

width = { '1': 2, '0': 4, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3 }

while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    total = len(N) + 1
    for num in N:
        total += width[num]
    print(total)
