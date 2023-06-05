import sys

first_rate, additional_rate = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
for _ in range(n):
    consumption = int(sys.stdin.readline())
    if consumption <= 1000:
        charge = first_rate * consumption
    else:
        charge = first_rate * 1000 + additional_rate * (consumption - 1000)
    print(f"{consumption} {charge}")
