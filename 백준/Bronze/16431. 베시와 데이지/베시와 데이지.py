import sys

Br, Bc = map(int, sys.stdin.readline().split())
Dr, Dc = map(int, sys.stdin.readline().split())
Jr, Jc = map(int, sys.stdin.readline().split())

Bessie = max(abs(Jr-Br), abs(Jc-Bc))
Daisy = abs(Jr-Dr) + abs(Jc-Dc)

if Bessie < Daisy:
    print('bessie')
elif Bessie > Daisy:
    print('daisy')
else:
    print('tie')
