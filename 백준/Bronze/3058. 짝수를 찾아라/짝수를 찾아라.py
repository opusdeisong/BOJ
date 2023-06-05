import sys

T = int(sys.stdin.readline())
for _ in range(T):
    numbers = list(map(int, sys.stdin.readline().split()))
    even_numbers = [number for number in numbers if number % 2 == 0]
    print(sum(even_numbers), min(even_numbers))
