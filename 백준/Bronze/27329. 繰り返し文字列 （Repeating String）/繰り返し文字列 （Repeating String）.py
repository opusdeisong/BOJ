import sys

N = int(sys.stdin.readline())

S = sys.stdin.readline().rstrip()

if S[:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")
