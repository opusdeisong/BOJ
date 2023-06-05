import sys

n = int(sys.stdin.readline())

while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    if num % n == 0:
        print(f'{num} is a multiple of {n}.')
    else:
        print(f'{num} is NOT a multiple of {n}.')
