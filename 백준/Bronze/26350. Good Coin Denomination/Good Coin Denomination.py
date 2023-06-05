import sys

n = int(sys.stdin.readline())

for _ in range(n):
    denom = list(map(int, sys.stdin.readline().split()))
    d = denom.pop(0)
    print("Denominations:", *denom)

    valid = True
    for i in range(1, d):
        if denom[i] < 2 * denom[i - 1]:
            valid = False
            break

    if valid:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")

    print()
