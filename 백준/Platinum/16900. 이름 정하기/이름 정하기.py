import sys

S, N = map(str, sys.stdin.readline().split())
N = int(N)

pi = [0] * len(S)
for i in range(1, len(S)):
    j = pi[i - 1]
    while j > 0 and S[i] != S[j]:
        j = pi[j - 1]
    if S[i] == S[j]:
        j += 1
    pi[i] = j

L = len(S)
print((N - 1) * (L - pi[L - 1]) + L)