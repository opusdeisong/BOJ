import sys

while True:
    a1, a2, a3 = map(int, sys.stdin.readline().split())
    if a1 == 0 and a2 == 0 and a3 == 0:
        break

    if a2 - a1 == a3 - a2:
        d = a2 - a1
        next_term = a3 + d
        print("AP", next_term)
    else:
        r = a2 // a1
        next_term = a3 * r
        print("GP", next_term)
