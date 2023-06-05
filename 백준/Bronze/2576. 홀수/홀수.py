import sys

numbers = [int(sys.stdin.readline()) for _ in range(7)]
odds = [num for num in numbers if num % 2 == 1]

if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
