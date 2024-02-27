import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
ans = 0

arr.sort()

left, right = 0, n - 1

while left < right:
    if arr[left] < 1 and arr[left + 1] < 1:
        ans += arr[left] * arr[left + 1]
        left += 2
    else:
        break

while right > 0:
    if arr[right] > 1 and arr[right - 1] > 1:
        ans += arr[right] * arr[right - 1]
        right -= 2
    else:
        break

for i in range(right, left-1, -1):
    ans += arr[i]

print(ans)