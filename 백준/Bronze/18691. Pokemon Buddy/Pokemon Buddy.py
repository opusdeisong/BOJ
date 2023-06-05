import sys

T = int(sys.stdin.readline())

for _ in range(T):
    G, C, E = map(int, sys.stdin.readline().split())

    if G == 1:
        candies_per_km = 1
    elif G == 2:
        candies_per_km = 1 / 3
    else:
        candies_per_km = 1 / 5

    required_candies = E - C
    if required_candies <= 0:
        print(0)
    else:
        print(int(required_candies / candies_per_km))
