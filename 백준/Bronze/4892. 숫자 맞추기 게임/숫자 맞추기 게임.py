import sys

case = 1
while True:
    n0 = int(sys.stdin.readline())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2 == 0:
        print(f"{case}. even {n1 // 2 // 3}")
    else:
        print(f"{case}. odd {(n1 + 1) // 2 // 3}")
    case += 1
