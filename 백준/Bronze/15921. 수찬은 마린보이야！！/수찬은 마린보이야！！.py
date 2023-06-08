import sys

N = int(sys.stdin.readline())
if N == 0:
    print("divide by zero")
else:
    records = list(map(int, sys.stdin.readline().split()))
    avg = sum(records) / N
    if avg == 0:
        print("divide by zero")
    else:
        print(format(1, ".2f"))
