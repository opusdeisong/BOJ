import sys

n, k = map(int, sys.stdin.readline().split())

segment = [0] * 300000


def init(start, end, node):
    if start == end:
        segment[node] = 1
        return 1

    mid = (start + end) // 2
    segment[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return segment[node]


def get_num_and_update(start, end, node, index):
    segment[node] -= 1
    if start == end:
        return start

    mid = (start + end) // 2
    if index > segment[node * 2]:
        return get_num_and_update(mid + 1, end, node * 2 + 1, index - segment[node * 2])
    else:
        return get_num_and_update(start, mid, node * 2, index)


init(1, n, 1)
idx = k - 1
print("<", end="")
for i in range(1, n + 1):
    get_idx = get_num_and_update(1, n, 1, idx + 1)

    if i != n:
        print(get_idx, end=", ")
    else:
        print(get_idx, end ="")

    if segment[1] == 0:
        break

    idx += k - 1
    idx %= segment[1]

print(">", end="")
