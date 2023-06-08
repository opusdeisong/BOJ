import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adjectives = [sys.stdin.readline().rstrip() for _ in range(n)]

nouns = [sys.stdin.readline().rstrip() for _ in range(m)]

for adjective in adjectives:
    for noun in nouns:
        print(f"{adjective} as {noun}")
