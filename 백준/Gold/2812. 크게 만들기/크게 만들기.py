import sys, heapq

N, K = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().strip()))
ans = []

for i in height:
    if not ans:
        ans.append(i)
        continue
    while ans and ans[-1] < i and K != 0:
        K -= 1
        ans.pop()
    ans.append(i)

while K != 0:
    K -= 1
    ans.pop()

for i in ans:
    print(i, end="")