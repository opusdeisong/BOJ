import sys

T = 1
while 1:
    L, P, V = map(int, sys.stdin.readline().split())
    if L + P + V == 0:
        break
    ans = (V // P) * L
    ans += min((V % P), L)
    print(f"Case {T}: {ans}")
    T += 1