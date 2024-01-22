import math
import sys


def init(node, start, end):
    if start == end:
        min_tree[node] = max_tree[node] = arr[start]
    else:
        init(node*2, start, (start + end) // 2)
        init(node*2 + 1, (start + end) // 2 + 1, end)
        min_tree[node] = min(min_tree[node*2], min_tree[node*2 + 1])
        max_tree[node] = max(max_tree[node*2], max_tree[node*2 + 1])

def find_min_max(node, start, end, left, right):
    if left > end or right < start:
        return (float('inf'), 0)
    elif left <= start and end <= right:
        return (min_tree[node], max_tree[node])
    else:
        l = find_min_max(node*2, start, (start + end) // 2, left, right)
        r = find_min_max(node*2 + 1, (start + end) // 2 + 1, end, left, right)
        return (min(l[0], r[0]), max(l[1], r[1]))

N, M = map(int, sys.stdin.readline().split())

h = int(math.ceil(math.log2(N)))
min_tree = [0] * (1 << (h + 1))
max_tree = [0] * (1 << (h + 1))

arr = [0] + [int(sys.stdin.readline()) for _ in range(N)]

init(1, 1, N)

for _ in range(M):
    left, right = map(int, sys.stdin.readline().split())
    result = find_min_max(1, 1, N, left, right)
    print(result[0], result[1])
