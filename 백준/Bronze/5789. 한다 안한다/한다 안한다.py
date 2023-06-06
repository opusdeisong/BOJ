import sys

T = int(sys.stdin.readline())

for _ in range(T):
    s = sys.stdin.readline().rstrip()
    if s[len(s) // 2] == s[len(s) // 2 - 1]:
        print('Do-it')
    else:
        print('Do-it-Not')
