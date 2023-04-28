import sys
import collections

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

NGE = [-1] * N
stack = collections.deque()

for i in range(N):
    while stack and (stack[-1][0] < A[i]):
        temp, index = stack.pop()
        NGE[index] = A[i]
    stack.append([A[i], i])

print(*NGE)