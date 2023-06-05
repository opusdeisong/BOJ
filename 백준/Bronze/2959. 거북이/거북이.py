import sys

A, B, C, D = map(int, sys.stdin.readline().split())

numbers = [A, B, C, D]
numbers.sort()

rectangle_area = numbers[0] * numbers[2]
print(rectangle_area)
