import sys


def check():
    global answer
    if stk[0][1] + stk[1][1] <= w and max(stk[0][0], stk[1][0]) <= h:
        answer = max(answer, stk[0][0]*stk[0][1] + stk[1][0]*stk[1][1])
    if stk[0][1] + stk[1][1] <= h and max(stk[0][0], stk[1][0]) <= w:
        answer = max(answer, stk[0][0]*stk[0][1] + stk[1][0]*stk[1][1])

def combination(idx, size, cnt):
    if cnt == 2:
        check()
        return
    for i in range(idx, size):
        nextR, nextC = sticker[i][0]
        stkNum = sticker[i][1]
        if visited[stkNum]:
            continue
        visited[stkNum] = True
        stk[cnt] = (nextR, nextC)
        combination(i + 1, size, cnt + 1)
        stk[cnt] = (0, 0)
        visited[stkNum] = False


h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
sticker = []
idx = 0
for i in range(n):
    r, c = map(int, sys.stdin.readline().split())
    sticker.append(((r, c), i))
    if r != c:
        sticker.append(((c, r), i))

visited = [False] * 100
stk = [(0, 0), (0, 0)]
answer = 0

combination(0, len(sticker), 0)
print(answer)
