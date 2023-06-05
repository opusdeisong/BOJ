import sys

A, B, C = map(int, sys.stdin.readline().split())

numbers = sorted([A, B, C])

if numbers[0] + numbers[1] == numbers[2]:
    print('S')
elif numbers[0] == numbers[1] or numbers[1] == numbers[2]:
    print('S')
else:
    print('N')
