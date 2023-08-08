import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    print(f"{N} => {N ** 2 - (N - 1)}")