import sys

S, K, H = map(int, sys.stdin.readline().split())

if (S + K + H)>= 100:
    print("OK")
else:
    small = min(S, K, H)
    if small == S:
        print("Soongsil")
    elif small == K:
        print("Korea")
    else:
        print("Hanyang")