import sys

T = int(sys.stdin.readline())
for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    print(sum(nums))