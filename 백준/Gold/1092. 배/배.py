import sys

N = int(sys.stdin.readline())
weight = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
M = int(sys.stdin.readline())
box = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
time = 0

if box[0] > weight[0]:
    print(-1)
    sys.exit()
while len(box) > 0:
    time += 1
    for i in range(len(weight)):
        for j in range(len(box)):
            if weight[i] >= box[j]:
                box.pop(j)
                break

print(time)