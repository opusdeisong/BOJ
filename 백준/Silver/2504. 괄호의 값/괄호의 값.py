import sys

given = list(sys.stdin.readline().rstrip())
stack = []
temp = 1
ans = 0
before = ""
for i in given:

    if i == "(":
        stack.append(i)
        temp *= 2

    elif i == "[":
        stack.append(i)
        temp *= 3

    elif i == ")":
        if len(stack) == 0 or stack [-1] == "[":
            ans = 0
            break
        elif before == "(":
            ans += temp
        stack.pop()
        temp = temp // 2

    elif i == "]":
        if len(stack) == 0 or stack [-1] == "(":
            ans = 0
            break
        elif before == "[":
            ans += temp
        stack.pop()
        temp = temp // 3

    before = i

if len(stack) == 0:
    print(ans)
else:
    print(0)