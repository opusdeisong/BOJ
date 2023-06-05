import sys

X, Y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

min_price_per_gram = X / Y

for _ in range(N):
    Xi, Yi = map(int, sys.stdin.readline().split())
    price_per_gram = Xi / Yi
    if price_per_gram < min_price_per_gram:
        min_price_per_gram = price_per_gram

print(f"{min_price_per_gram * 1000:.2f}")
