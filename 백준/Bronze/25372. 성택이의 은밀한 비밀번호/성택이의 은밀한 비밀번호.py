import sys

N = int(sys.stdin.readline())
for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    ans = len(temp)
    if ans >= 6 and ans <= 9:
        print('yes')
    else:
        print('no')