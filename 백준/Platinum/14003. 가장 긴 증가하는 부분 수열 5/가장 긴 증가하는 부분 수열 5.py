import sys, bisect

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = []
temp = []

for i in A:
    if not dp or i > dp[-1]:
        dp.append(i)
        temp.append((len(dp) - 1, i))
    else:
        dp[bisect.bisect_left(dp, i)] = i
        temp.append((bisect.bisect_left(dp, i), i))

ans = []
ans_idx = len(dp) - 1

for i in range(len(temp) - 1, -1, -1):
    if temp[i][0] == ans_idx:
        ans.append(temp[i][1])
        ans_idx -= 1

ans.reverse()
print(len(ans))
print(*ans)