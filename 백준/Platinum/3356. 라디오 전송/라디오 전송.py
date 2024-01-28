import sys

t = 1
N = int(sys.stdin.readline())

S = sys.stdin.readline().rstrip()

pi = [0] * len(S)
for i in range(1, len(S)):
    j = pi[i - 1]
    while j > 0 and S[i] != S[j]:
        j = pi[j - 1]
    if S[i] == S[j]:
        j += 1
    pi[i] = j

L = len(S)
print(L-pi[-1])
t += 1