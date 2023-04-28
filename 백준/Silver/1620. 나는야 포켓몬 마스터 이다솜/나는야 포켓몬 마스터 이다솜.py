import sys
N, M = map(int, sys.stdin.readline().split())
pokemon = {}
for _ in range(N):
    temp = (sys.stdin.readline()).rstrip()
    pokemon[_ + 1] = temp
    pokemon[temp] = _ + 1
for i in range(M):
    K = sys.stdin.readline().rstrip()
    if K.isdigit():
        print(pokemon[int(K)])
    else:
        print(pokemon[K])