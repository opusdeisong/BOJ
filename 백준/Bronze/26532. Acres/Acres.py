import math
g, p = map(int, input().split())
temp = g * p
acr = 4840 * 5
print(math.ceil(temp / acr))