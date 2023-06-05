import sys

for _ in range(3):
    N = int(sys.stdin.readline())
    sum = 0
    for _ in range(N):
        sum += int(sys.stdin.readline())
    if sum == 0:
        print("0")
    elif sum > 0:
        print("+")
    else:
        print("-")
