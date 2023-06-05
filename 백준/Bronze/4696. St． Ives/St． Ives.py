import sys

while True:
    n = float(sys.stdin.readline())
    if n == 0:
        break
    total = 1 + n * (1 + n * (1 + n * (1 + n)))
    print(f'{total:.2f}')
