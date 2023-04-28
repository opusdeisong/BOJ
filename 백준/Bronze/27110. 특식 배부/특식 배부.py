import sys
N = int(sys.stdin.readline())
A, B, C = map(int, sys.stdin.readline().split())
sum = 0
if A > N:
    sum += N
else:
    sum += A

if B > N:
    sum += N
else:
    sum += B

if C > N:
    sum += N
else:
    sum += C
    
print(sum)