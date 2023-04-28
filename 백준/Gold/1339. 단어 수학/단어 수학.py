import sys

N = int(sys.stdin.readline())
alphabet = [(sys.stdin.readline().strip()) for _ in range(N)]
match = {}
num = []

for i in range(N):
    for j in range(len(alphabet[i])):
        if alphabet[i][j] in match:
            match[alphabet[i][j]] += 10 ** (len(alphabet[i]) - j - 1)
        else:
            match[alphabet[i][j]] = 10 ** (len(alphabet[i]) - j - 1)

for i in match.values():
    num.append(i)

num.sort()
ans = 0
temp = 9 - len(num) + 1
for i in num:
    ans += temp * i
    temp += 1

print(ans)