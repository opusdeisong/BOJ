import sys

numbers = sorted(list(map(int, sys.stdin.readline().split())))


if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    print(numbers[2] + (numbers[1] - numbers[0]))
elif numbers[2] - numbers[1] > numbers[1] - numbers[0]:
    print(numbers[1] + (numbers[1] - numbers[0]))
else:
    print(numbers[0] + (numbers[2] - numbers[1]))
