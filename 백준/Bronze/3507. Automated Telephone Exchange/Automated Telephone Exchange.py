import sys

N = int(sys.stdin.readline())

if N > 198:
    print(0)
else:
    print(199 - N)