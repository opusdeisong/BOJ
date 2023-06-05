import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    if i % 2 == 1:
        print("* " * N)
    else:
        print(" *" * N)
