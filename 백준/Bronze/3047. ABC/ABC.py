import sys

numbers = list(map(int, sys.stdin.readline().split()))
order = sys.stdin.readline().rstrip()

numbers.sort()

for char in order:
    if char == 'A':
        print(numbers[0], end=' ')
    elif char == 'B':
        print(numbers[1], end=' ')
    elif char == 'C':
        print(numbers[2], end=' ')
