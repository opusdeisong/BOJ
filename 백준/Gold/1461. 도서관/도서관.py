import sys

def calc(temp, M, ans):
    while len(temp) >= M:
        ans += abs(temp[0]) * 2
        for _ in range(M):
            temp.pop(0)
    if len(temp) != 0:
        ans += abs(temp[0]) * 2
    return ans

N, M = map(int, sys.stdin.readline().split())
book = list(map(int, sys.stdin.readline().split()))
book.sort()
book_pos = []
book_neg = []
for i in book:
    if i < 0:
        book_neg.append(i)
    else:
        book_pos.insert(0, i)
if len(book_neg) and len(book_pos):
    big = max(abs(book_neg[0]), book_pos[0])
elif len(book_pos):
    big = abs(book_pos[0])
else:
    big = abs(book_neg[0])
ans = 0
ans = calc(book_pos, M, ans)
ans = calc(book_neg, M, ans)
print(ans - big)
