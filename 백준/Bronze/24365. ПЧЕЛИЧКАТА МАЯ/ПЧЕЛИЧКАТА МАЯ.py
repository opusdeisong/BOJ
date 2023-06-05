import sys

arr = [(0,0), (0,1), (0,2)]
a, b, c = map(int, sys.stdin.readline().split())
arr[0] = (a, 0)
arr[1] = (b, 1)
arr[2] = (c, 2)

avg = (arr[0][0] + arr[1][0] + arr[2][0]) // 3

arr = sorted(arr)

ans = abs(arr[2][1] - arr[0][1]) * (avg - arr[0][0]) + abs(arr[2][1] - arr[1][1]) * (avg - arr[1][0])

print(ans)
