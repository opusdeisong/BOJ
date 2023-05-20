import sys

N, M = map(int, sys.stdin.readline().split())
if M <= 2:
    print("NEWBIE!")
elif M > 2 and M <= N:
    print("OLDBIE!")
else:
    print("TLE!")