import sys

L, R = map(str, sys.stdin.readline().split())

ans = 0

if len(L)== len(R):
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                ans += 1
        else:
            break

    print(ans)
else:
    print(0)