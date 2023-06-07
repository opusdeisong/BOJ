import sys

buttons = list(map(int, sys.stdin.readline().split()))
total_cost = 0
for button in buttons:
    if button == 1:
        total_cost += 500
    elif button == 2:
        total_cost += 800
    elif button == 3:
        total_cost += 1000
change = 5000 - total_cost
print(change)
