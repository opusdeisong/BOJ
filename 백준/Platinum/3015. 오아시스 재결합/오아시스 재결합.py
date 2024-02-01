import sys

people_num = int(sys.stdin.readline())
stack = []
cnt_pair = 0

for _ in range(people_num):
    now = int(sys.stdin.readline())
    cnt_same_height = 1

    while stack and stack[-1][0] < now:
        cnt_pair += stack[-1][1]
        stack.pop()

    if stack:
        if stack[-1][0] == now:
            cnt_pair += stack[-1][1]
            cnt_same_height = stack[-1][1] + 1
            if len(stack) > 1:
                cnt_pair += 1
            stack.pop()
        else:
            cnt_pair += 1

    stack.append((now, cnt_same_height))

print(cnt_pair)