import sys, heapq

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
while S != T and len(T) != 0:
    if T[-1] == 'A':
        T = T[:len(T) - 1]
    else:
        T = list(T[:len(T) - 1])
        T.reverse()
        T = ''.join(T)
if S == T:
    print(1)
else:
    print(0)