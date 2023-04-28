import sys
A, B = map(int,sys.stdin.readline().split())

ans = (A + B) * (A - B)
print(ans)