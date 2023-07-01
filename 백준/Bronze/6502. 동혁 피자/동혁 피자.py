import math, sys

cnt = 1

while True:
    arr = list(map(int, sys.stdin.readline().split()))
    x = arr[0]

    if x == 0:
        break

    y, z = arr[1], arr[2]

    if x >= math.sqrt(z / 2 * z / 2 + y / 2 * y / 2):
        print(f"Pizza {cnt} fits on the table.")
    else:
        print(f"Pizza {cnt} does not fit on the table.")

    cnt += 1
