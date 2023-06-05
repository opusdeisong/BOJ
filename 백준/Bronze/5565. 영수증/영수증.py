import sys

total_price = int(sys.stdin.readline())
known_prices_sum = sum(int(sys.stdin.readline()) for _ in range(9))

unknown_price = total_price - known_prices_sum
print(unknown_price)
