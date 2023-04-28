import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = input()
t = len(arr[0])
togo = 0
for i in range(1, t + 1):
    ans = []
    for j in range(N):
        if arr[j][- i:] not in ans:
            ans.append(arr[j][- i:])
    if len(ans) == N:
        togo = i
        break
print(i)