import math
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    price = float(sys.stdin.readline())
    discount = price * 0.2
    discounted_price = price - discount
    rounded_price = round(discounted_price, 2)

    print("${:.2f}".format(rounded_price))
