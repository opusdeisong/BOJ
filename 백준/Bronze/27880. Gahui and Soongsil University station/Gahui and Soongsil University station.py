import sys

ans = 0
for _ in range(4):
    arr = sys.stdin.readline().split()
    if arr[0] == 'Es':
        ans += 21 * int(arr[1])
    else:
        ans += 17 * int(arr[1])
print(ans)