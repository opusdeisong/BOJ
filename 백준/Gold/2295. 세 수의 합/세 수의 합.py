import sys

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()

nums = set()

for i in num:
    for j in num:
        nums.add(i + j)

ans = []

for i in num:
    for j in num:
        if i - j in nums:
            ans.append(i)
ans.sort()
print(ans[-1])