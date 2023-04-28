import sys

def push(que, n):
    que.append(n)

def push_f(que, n):
    que.insert(0, n)

def pop_f(que):
    if len(que) == 0:
        print(-1)
    else:
        print(que[0])
        que.remove(que[0])

def pop_b(que):
    if len(que) == 0:
        print(-1)
    else:
        print(que.pop(len(que) - 1))

def size(que):
    print(len(que))

def empty(que):
    if len(que) == 0:
        print(1)
    else:
        print(0)

def front(que):
    if len(que) == 0:
        print(-1)
    else:
        print(que[0])

def back(que):
    if len(que) == 0:
        print(-1)
    else:
        print(que[-1])

N = int(sys.stdin.readline())
que = []

for _ in range(N):
    comm = sys.stdin.readline().split()
    if len(comm) == 2:
        if comm[0] == 'push_back':
            push(que, comm[1])
        else:
            push_f(que, comm[1])
    else:
        if comm[0] == 'pop_front':
            pop_f(que)
        elif comm[0] == 'pop_back':
            pop_b(que)
        elif comm[0] == 'size':
            size(que)
        elif comm[0] == 'empty':
            empty(que)
        elif comm[0] == 'front':
            front(que)
        elif comm[0] == 'back':
            back(que)