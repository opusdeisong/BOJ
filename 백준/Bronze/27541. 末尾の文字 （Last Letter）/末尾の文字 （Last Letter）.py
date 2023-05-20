import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

if S[-1] == 'G':
    result = S[:-1]
else:
    result = S + 'G'

print(result)
