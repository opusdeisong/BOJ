import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
max_cars = m
for _ in range(n):
    in_cars, out_cars = map(int, sys.stdin.readline().split())
    m = m + in_cars - out_cars
    if m < 0:
        print(0)
        break
    max_cars = max(max_cars, m)
else:
    print(max_cars)
