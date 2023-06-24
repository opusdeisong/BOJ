import sys


def insert(ant_den, foods):
    current = ant_den
    for food in foods:
        if food not in current:
            current[food] = {}
        current = current[food]


def output(ant_den, depth):
    for food, next_ant_den in sorted(ant_den.items()):
        print('--' * depth + food)
        output(next_ant_den, depth + 1)


n = int(sys.stdin.readline())
root = {}

for _ in range(n):
    k, *foods = sys.stdin.readline().split()
    insert(root, foods)

output(root, 0)
