import sys

INF = float('inf')

class Node:
    def __init__(self, num=INF, idx=INF):
        self.num = num
        self.idx = idx

    def __lt__(self, other):
        if self.num == other.num:
            return self.idx < other.idx
        return self.num < other.num

def query(start, end, node, left, right):
    if left > end or start > right:
        return Node()
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query(start, mid, node * 2, left, right), query(mid + 1, end, node * 2 + 1, left, right))

def update(start, end, node, index, y):
    if index < start or index > end:
        return tree[node]
    if start == end:
        tree[node] = Node(y, index)
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(
        update(start, mid, node * 2, index, y),
        update(mid + 1, end, node * 2 + 1, index, y)
    )
    return tree[node]

def init(start, end, node):
    if start == end:
        tree[node] = Node(a[start], start)
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1))
    return tree[node]

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
tree = [Node() for _ in range(4 * n)]

q = int(sys.stdin.readline())
init(0, n - 1, 1)
for _ in range(q):
    op, x, y = map(int, sys.stdin.readline().split())
    if op == 1:
        update(0, n - 1, 1, x - 1, y)
    else:
        print(query(0, n - 1, 1, x - 1, y - 1).idx + 1)
