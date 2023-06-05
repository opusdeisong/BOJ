import sys

N = int(sys.stdin.readline())
bin_N = bin(N)[2:]
if bin_N.count('1') == 1:
    print(1)
else:
    print(0)

