import sys

p1, s1 = map(int, sys.stdin.readline().split())
s2, p2 = map(int, sys.stdin.readline().split())

if p1 + p2 == s1 + s2:
    if p1 == s2:
        print("Penalty")
    elif p1 > s2:
        print("Esteghlal")
    else:
        print("Persepolis")
elif p1 + p2 < s1 + s2:
    print("Esteghlal")
else:
    print("Persepolis")
