import sys

ans = dict()

for _ in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    if b == 'enter':
        ans[a] = True
    else:
        del ans[a]
anss = sorted(ans.keys(), reverse=True)
for i in anss:
    print(i)